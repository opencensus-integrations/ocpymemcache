# ocpymemcache

PyMemcache Python wrapper with observability provided by OpenCensus
instrumented with tracing and metrics.

The mettrics recorded include:
* calls
* latency in milliseconds

Metric|View name|Unit|Tags
---|---|---|---
Latency|"pymemcache/latency"|"ms"|"error", "method", "status"
Calls|"pymemcache/calls"|"1"|"error", "method", "status"
