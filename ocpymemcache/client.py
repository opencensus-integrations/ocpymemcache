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

from pymemcache.client.base import Client as PyMemcacheClient
from ocpymemcache.observability import TrackingOperation

class OCPyMemcacheClient(object):
    """
    OCPyMemcacheClient is the instrumented wrapper to provide
    traces and metrics to a pymemache.client.base.Client instance.
    It takes the exact arguments that a HashClient would take and
    underlyingly creates the client which it then wraps.
    The same usage pattern for the original client would apply here.
    """
    
    __TRACKING_OPERATION = TrackingOperation()

    def __init__(self, server_addr, *args, **kwargs):
        self.__pymc = PyMemcacheClient(server_addr, *args, **kwargs)

    def add(self, key, value, *args, **kwargs):
        return self.__TRACKING_OPERATION.trace_and_record_stats(
                'pymemcache.client.base.Client.add',
                self.__pymc.add, key, value, *args, **kwargs)
        
    def append(self, key, value, *args, **kwargs):
        return self.__TRACKING_OPERATION.trace_and_record_stats(
                'pymemcache.client.base.Client.append',
                self.__pymc.append, key, value, *args, **kwargs)

    def cas(self, key, value, cas, *args, **kwargs):
        return self.__TRACKING_OPERATION.trace_and_record_stats(
                'pymemcache.client.base.Client.cas',
                self.__pymc.cas, key, value, *args, **kwargs)

    def check_key(self, key):
        # Does not touch the remote end.
        return self.__pymc.check_key(key)

    def close(self):
        return self.__TRACKING_OPERATION.trace_and_record_stats(
                'pymemcache.client.base.Client.close',
                self.__pymc.close)

    def decr(self, key, value, *args, **kwargs):
        return self.__TRACKING_OPERATION.trace_and_record_stats(
                'pymemcache.client.base.Client.decr',
                self.__pymc.decr, key, value, *args, **kwargs)

    def delete(self, key, *args, **kwargs):
        return self.__TRACKING_OPERATION.trace_and_record_stats(
                'pymemcache.client.base.Client.delete',
                self.__pymc.delete, key, *args, **kwargs)

    def delete_many(self, keys, *args, **kwargs):
        return self.__TRACKING_OPERATION.trace_and_record_stats(
                'pymemcache.client.base.Client.delete_many',
                self.__pymc.delete_many, keys, *args, **kwargs)

    def delete_multi(self, keys, *args, **kwargs):
        return self.__TRACKING_OPERATION.trace_and_record_stats(
                'pymemcache.client.base.Client.delete_multi',
                self.__pymc.delete_multi, keys, *args, **kwargs)

    def flush_all(self, *args, **kwargs):
        return self.__TRACKING_OPERATION.trace_and_record_stats(
                'pymemcache.client.base.Client.flush_all',
                self.__pymc.flush_all, *args, **kwargs)

    def get(self, key, *args, **kwargs):
        return self.__TRACKING_OPERATION.trace_and_record_stats(
                'pymemcache.client.base.Client.get',
                self.__pymc.get, key, *args, **kwargs)

    def get_many(self, keys, *args, **kwargs):
        return self.__TRACKING_OPERATION.trace_and_record_stats(
                'pymemcache.client.base.Client.get_many',
                self.__pymc.get_many, key, *args, **kwargs)

    def get_multi(self, keys, *args, **kwargs):
        return self.__TRACKING_OPERATION.trace_and_record_stats(
                'pymemcache.client.base.Client.get_multi',
                self.__pymc.get_multi, key, *args, **kwargs)

    def gets(self, keys, *args, **kwargs):
        return self.__TRACKING_OPERATION.trace_and_record_stats(
                'pymemcache.client.base.Client.gets',
                self.__pymc.gets, keys, *args, **kwargs)

    def gets_many(self, keys, *args, **kwargs):
        return self.__TRACKING_OPERATION.trace_and_record_stats(
                'pymemcache.client.base.Client.gets_many',
                self.__pymc.gets_many, keys, *args, **kwargs)

    def incr(self, key, value, *args, **kwargs):
        return self.__TRACKING_OPERATION.trace_and_record_stats(
                'pymemcache.client.base.Client.incr',
                self.__pymc.incr, key, value, *args, **kwargs)

    def prepend(self, key, value, *args, **kwargs):
        return self.__TRACKING_OPERATION.trace_and_record_stats(
                'pymemcache.client.base.Client.prepend',
                self.__pymc.prepend, key, value, *args, **kwargs)

    def quit(self, *args, **kwargs):
        return self.__TRACKING_OPERATION.trace_and_record_stats(
                'pymemcache.client.base.Client.quit',
                self.__pymc.quit, *args, **kwargs)

    def replace(self, key, value, *args, **kwargs):
        return self.__TRACKING_OPERATION.trace_and_record_stats(
                'pymemcache.client.base.Client.replace',
                self.__pymc.replace, key, value, *args, **kwargs)

    def set(self, key, value, *args, **kwargs):
        return self.__TRACKING_OPERATION.trace_and_record_stats(
                'pymemcache.client.base.Client.set',
                self.__pymc.set, key, value, *args, **kwargs)

    def set_many(self, values, *args, **kwargs):
        return self.__TRACKING_OPERATION.trace_and_record_stats(
                'pymemcache.client.base.Client.set_many',
                self.__pymc.set_many, values, *args, **kwargs)

    def set_multi(self, values, *args, **kwargs):
        return self.__TRACKING_OPERATION.trace_and_record_stats(
                'pymemcache.client.base.Client.set_multi',
                self.__pymc.set_multi, values, *args, **kwargs)

    def stats(self, *args):
        return self.__TRACKING_OPERATION.trace_and_record_stats(
                'pymemcache.client.base.Client.stats',
                self.__pymc.stats, *args)

    def touch(self, key, *args, **kwargs):
        return self.__TRACKING_OPERATION.trace_and_record_stats(
                'pymemcache.client.base.Client.touch',
                self.__pymc.touch, *args, **kwargs)

    def version(self):
        return self.__TRACKING_OPERATION.trace_and_record_stats(
                'pymemcache.client.base.Client.version',
                self.__pymc.version)
