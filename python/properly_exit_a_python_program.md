# Properly Exit A Python Program
In python they are several ways to exit a python program.

In a nutshell (read further for more details), the recommended way to
explicitely terminate a python program is:
- call `sys.exit` without hesitation in case the program is mono-threaded
    (most cases). It is possible to run clean up actions by catching the
    `SystemExit` exception
- check that `SystemExit` is well managed (that is can bubble up to the main
    thread) if the python program is multi-threaded or make sure to always call
    `sys.exit` from the `main thread`
- otherwise, call `os._exit` which terminates a process no matter which thread
    called it. However, as this is a system call, no user-space-code can be run
    to execute some clean up procedure.

## The program ran successfuly until completion
Every instructions are run, the program completes then return `0` on linux 
and unix plateforms.

## The program terminates due to an uncaught exception
An exception has been raised but not caught by any user code.

The python interpreter catches any uncaught exception, calls
`__at_exit__` then returns a non zero error code.

### Gotcha
The `__at_exit__` function gets called only if the exception was raised in
the `main thread`! Meaning that a multi-threaded-python-program will only
be terminated by an exception if it got uncaught in the main thread.

If such an exception is raised in another thread and is not caught in that thread,
then the thread is terminated (not the whole process!).

## Call os._exit
`os._exit` is OS-dependent, it calls a system call to terminate a process. If the
call is available on the platform, it is sure that the call will terminate the process.

However, as being an action carried by the OS, not from python no python-cleanup-actions
can be run before the process terminates.

This makes it a less suitable as calling `sys.exit`.

*IMPORTANT:* `os._exit` terminates a python process no matter which thread it has been called
from.

## Call sys.exit
`sys.exit` actually raises a `SystemExit` exception, which therefore causes
the program to stop.

`sys.exit` can take an error code so that the scripts return code value can be
set.

``` python
import sys

# OK no problem
sys.exit(0)

# Some error happened
sys.exit(1)
```

*IMPORTANT:* `sys.exit` has the same problem as terminating a program from an uncaught
exception as an exception is raised to try to stop the process. However, if the process
is mono-threaded, then calling `sys.exit` is the best practice as it offers the possibility
to do some cleanup before exiting (as per exceptions' design).

## Call builtin exit function
`exit` is a function from the `site` module. This module is loaded into the `__builtins__`
module when starting up the python interpreter.

However, functions implemented in the `site` modules are made for python running in interactive
interpreter mode. They are explicitely not recommended by the python documentation:

```
The site module (which is imported automatically during startup, except if the -S command-line
option is given) adds several constants to the built-in namespace. They are useful for the
interactive interpreter shell and should not be used in programs.
```

Furthermore, `exit` or `quit` acts as aliases of `sys.exit` as they attempt to terminate python
programs by raising a `SystemExit` exception. This is exactly the same behaviour as `sys.exit`.

In conclusion, it is bad practice to use `exit` or `quit` in a python program. Use `sys.exit`
or `os._exit` instead.

