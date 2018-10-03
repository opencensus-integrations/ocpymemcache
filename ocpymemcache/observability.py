# Copyright 2018, OpenCensus Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import time

from opencensus.trace.status import Status
from opencensus.trace.tracer import Tracer

from opencensus.stats import stats
from opencensus.stats import aggregation as aggregation_module
from opencensus.stats import measure as measure_module
from opencensus.stats import view as view_module
from opencensus.tags import tag_key as tag_key_module
from opencensus.tags import tag_map as tag_map_module
from opencensus.tags import tag_value as tag_value_module

key_method = tag_key_module.TagKey("method")
key_error  = tag_key_module.TagKey("error")
key_status = tag_key_module.TagKey("status")

m_latency_ms = measure_module.MeasureFloat("pymemcache/latency", "The latency in milliseconds per method", "ms")
m_calls = measure_module.MeasureInt("pymemcache/calls", "The number of calls made", "1")

def enable_metrics_views():
    calls_view = view_module.View("pymemcache/calls", "The number of calls",
        [key_method, key_error, key_status],
        m_calls,
        aggregation_module.CountAggregation())

    latency_view = view_module.View("pymemcache/latency", "The distribution of the latencies",
        [key_method, key_error, key_status],
        m_latency_ms,
        aggregation_module.DistributionAggregation([
	    # Latency in buckets:
	    # [>=0ms, >=5ms, >=10ms, >=25ms, >=40ms, >=50ms, >=75ms, >=100ms, >=200ms, >=400ms, >=600ms, >=800ms, >=1s, >=2s, >=4s, >=6s, >=10s, >-20s]
            0, 5, 10, 25, 40, 50, 75, 100, 200, 400, 600, 800, 1000, 2000, 4000, 6000, 10000, 20000
        ]))

    view_manager = stats.Stats().view_manager
    view_manager.register_view(calls_view)
    view_manager.register_view(latency_view)

class TrackingOperation(object):
    __TRACER = Tracer()
    __STATS_RECORDER = stats.Stats().stats_recorder

    def __init__(self):
        pass

    def trace_and_record_stats(self, method_name, fn, *args, **kwargs):
        start_time = time.time()

        tags = tag_map_module.TagMap()
        tags.insert(key_method, tag_value_module.TagValue(method_name))
        mm = self.__STATS_RECORDER.new_measurement_map()

        with self.__TRACER.span(name=method_name) as span:
            try:
                return fn(*args, **kwargs)
            except Exception as e: # an error to record
                span.status = Status.from_exception(e)
                # TODO: (@odeke-em) perhaps shorten the exception when added as a tag here?
                tags.insert(key_error, e.__str__())
                # Then finally after recording the exception, re-raise it.
                raise e
            else: # Success
                tags.insert(key_status, "ok")
            finally:
                latency_ms = (time.time() - start_time) * 1000
                mm.measure_float_put(m_latency_ms, latency_ms)
                mm.measure_int_put(m_calls, 1)
                mm.record(tags)
