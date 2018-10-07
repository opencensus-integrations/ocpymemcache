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

from pymemcache.client.hash import HashClient as PyMemcacheHashClient
from ocpymemcache.observability import TrackingOperation

class OCPyMemcacheHashClient(object):
    """
    OCPyMemcacheHashClient is the instrumented wrapper to provide
    traces and metrics to a pymemache.client.hash.HashClient instance.
    It takes the exact arguments that a HashClient would take and
    underlyingly creates the client which it then wraps.
    The same usage pattern for the original client would apply here.
    """
    
    __TRACKING_OPERATION = TrackingOperation()

    def __init__(self, servers, *args, **kwargs):
        self.__pyhmc = PyMemcacheHashClient(servers, *args, **kwargs)

    def add(self, key, value, *args, **kwargs):
        return self.__TRACKING_OPERATION.trace_and_record_stats(
                'pymemcache.client.hash.HashClient.add',
                self.__pyhmc.add, key, value, *args, **kwargs)
        
    def append(self, key, value, *args, **kwargs):
        return self.__TRACKING_OPERATION.trace_and_record_stats(
                'pymemcache.client.hash.HashClient.append',
                self.__pyhmc.append, key, value, *args, **kwargs)

    def cas(self, key, value, cas, *args, **kwargs):
        return self.__TRACKING_OPERATION.trace_and_record_stats(
                'pymemcache.client.hash.HashClient.cas',
                self.__pyhmc.cas, key, value, *args, **kwargs)

    def check_key(self, key):
        # Does not touch the remote end.
        return self.__pyhmc.check_key(key)

    def close(self):
        return self.__TRACKING_OPERATION.trace_and_record_stats(
                'pymemcache.client.hash.HashClient.close',
                self.__pyhmc.close)

    def decr(self, key, value, *args, **kwargs):
        return self.__TRACKING_OPERATION.trace_and_record_stats(
                'pymemcache.client.hash.HashClient.decr',
                self.__pyhmc.decr, key, value, *args, **kwargs)

    def delete(self, key, *args, **kwargs):
        return self.__TRACKING_OPERATION.trace_and_record_stats(
                'pymemcache.client.hash.HashClient.delete',
                self.__pymc.delete, key, *args, **kwargs)

    def delete_many(self, keys, *args, **kwargs):
        return self.__TRACKING_OPERATION.trace_and_record_stats(
                'pymemcache.client.hash.HashClient.delete_many',
                self.__pyhmc.delete_many, keys, *args, **kwargs)

    def delete_multi(self, keys, *args, **kwargs):
        return self.__TRACKING_OPERATION.trace_and_record_stats(
                'pymemcache.client.hash.HashClient.delete_multi',
                self.__pyhmc.delete_multi, keys, *args, **kwargs)

    def flush_all(self, *args, **kwargs):
        return self.__TRACKING_OPERATION.trace_and_record_stats(
                'pymemcache.client.hash.HashClient.flush_all',
                self.__pyhmc.flush_all, *args, **kwargs)

    def get(self, key, *args, **kwargs):
        return self.__TRACKING_OPERATION.trace_and_record_stats(
                'pymemcache.client.hash.HashClient.get',
                self.__pyhmc.get, key, *args, **kwargs)

    def get_many(self, keys, *args, **kwargs):
        return self.__TRACKING_OPERATION.trace_and_record_stats(
                'pymemcache.client.hash.HashClient.get_many',
                self.__pyhmc.get_many, key, *args, **kwargs)

    def get_multi(self, keys, *args, **kwargs):
        return self.__TRACKING_OPERATION.trace_and_record_stats(
                'pymemcache.client.hash.HashClient.get_multi',
                self.__pyhmc.get_multi, key, *args, **kwargs)

    def gets(self, keys, *args, **kwargs):
        return self.__TRACKING_OPERATION.trace_and_record_stats(
                'pymemcache.client.hash.HashClient.gets',
                self.__pyhmc.gets, keys, *args, **kwargs)

    def gets_many(self, keys, *args, **kwargs):
        return self.__TRACKING_OPERATION.trace_and_record_stats(
                'pymemcache.client.hash.HashClient.gets_many',
                self.__pyhmc.gets_many, keys, *args, **kwargs)

    def incr(self, key, value, *args, **kwargs):
        return self.__TRACKING_OPERATION.trace_and_record_stats(
                'pymemcache.client.hash.HashClient.incr',
                self.__pyhmc.incr, key, value, *args, **kwargs)

    def prepend(self, key, value, *args, **kwargs):
        return self.__TRACKING_OPERATION.trace_and_record_stats(
                'pymemcache.client.hash.HashClient.prepend',
                self.__pyhmc.prepend, key, value, *args, **kwargs)

    def quit(self, *args, **kwargs):
        return self.__TRACKING_OPERATION.trace_and_record_stats(
                'pymemcache.client.hash.HashClient.quit',
                self.__pyhmc.quit, *args, **kwargs)

    def replace(self, key, value, *args, **kwargs):
        return self.__TRACKING_OPERATION.trace_and_record_stats(
                'pymemcache.client.hash.HashClient.replace',
                self.__pyhmc.replace, key, value, *args, **kwargs)

    def set(self, key, value, *args, **kwargs):
        return self.__TRACKING_OPERATION.trace_and_record_stats(
                'pymemcache.client.hash.HashClient.set',
                self.__pyhmc.set, key, value, *args, **kwargs)

    def set_many(self, values, *args, **kwargs):
        return self.__TRACKING_OPERATION.trace_and_record_stats(
                'pymemcache.client.hash.HashClient.set_many',
                self.__pyhmc.set_many, values, *args, **kwargs)

    def set_multi(self, values, *args, **kwargs):
        return self.__TRACKING_OPERATION.trace_and_record_stats(
                'pymemcache.client.hash.HashClient.set_multi',
                self.__pyhmc.set_multi, values, *args, **kwargs)

    def stats(self, *args):
        return self.__TRACKING_OPERATION.trace_and_record_stats(
                'pymemcache.client.hash.HashClient.stats',
                self.__pyhmc.stats, *args)

    def touch(self, key, *args, **kwargs):
        return self.__TRACKING_OPERATION.trace_and_record_stats(
                'pymemcache.client.hash.HashClient.touch',
                self.__pyhmc.touch, *args, **kwargs)

    def version(self):
        return self.__TRACKING_OPERATION.trace_and_record_stats(
                'pymemcache.client.hash.HashClient.version',
                self.__pyhmc.version)
