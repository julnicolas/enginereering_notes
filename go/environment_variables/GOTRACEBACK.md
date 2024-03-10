# GOTRACEBACK

Generate a crash dump for supported platforms.
``` sh
export GOTRACEBACK=crash
```

## Details
The GOTRACEBACK variable controls the amount of output generated 
when a Go program fails due to an unrecovered panic or 
an unexpected runtime condition. By default, a failure 
prints a stack trace for the current goroutine, eliding 
functions internal to the run-time system, and 
then exits with exit code 2. The failure prints 
stack traces for all goroutines if there is no current 
goroutine or the failure is internal to the run-time. 
`GOTRACEBACK=none` omits the goroutine stack traces 
entirely. `GOTRACEBACK=single` (the default) behaves 
as described above. `GOTRACEBACK=all` adds stack traces 
for all user-created goroutines. `GOTRACEBACK=system` 
is like “all” but adds stack frames for 
run-time functions and shows goroutines created internally by 
the run-time. `GOTRACEBACK=crash` is like 
“system” but crashes in an operating system-
specific manner instead of exiting. For example, on 
Unix systems, the crash raises `SIGABRT` to trigger a 
core dump. `GOTRACEBACK=wer` is like “crash
” but doesn't disable Windows Error Reporting (
WER). For historical reasons, the GOTRACEBACK settings 0, 1, and 2 
are synonyms for none, all, and system, respectively. 
The `runtime/debug.SetTraceback function allows increasing 
the amount of output at run time, but it cannot reduce the amount 
below that specified by the environment variable. 
