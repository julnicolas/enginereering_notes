# Enable Memory Profiling

``` sh
pip install memray
```

To capture a memory profile for a script.
Run memray with the following command:

``` sh
memray run [-m] <module_or_python_script>
```

This will generate a capture file, processable
to export various kind of exports (flamegraphs,
tables, summaries, statistics).

It is possible to run it in live mode:
``` sh
memray run --live [-m] <module_or_python_script>
```

