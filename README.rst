ocpymemcache
=============

PyMemcache Python wrapper with observability provided by OpenCensus
instrumented with tracing and metrics.

The mettrics recorded include:

- calls
- latency in milliseconds

.. csv-table::
   :header: "Metric", "View Name", "Unit", "Tags"
   :widths: 20, 20, 20, 20

   "Latency", "pymemcache/latency", "ms", "'error', 'method', 'status'"
   "Calls", "pymemcache/calls", "1", "'error', 'method', 'status'"

Installing it
-------------

pip install ocpymemcache
