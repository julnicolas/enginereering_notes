# Builtin object listing

All the objects below are imported when starting a python program... with a few exceptions!

If python is started in interactive mode, then the `site` package is also loaded in addition to
the `builtins` package.

This site package defines the following additional functions:
- `exit` a wrapper of sys.exit, with a warn message if called from a python interpreter 
	not in interactive mode
- `quit` (an alias of `exit`)
- `copyright`
- `credits`
- `licence`
- `help`

These functions are defined for interpreter environments, they are not recommended for use
by python programs according to the python documentation:

```
The site module (which is imported automatically during startup, except if the -S 
command-line option is given) adds several constants to the built-in namespace.
They are useful for the interactive interpreter shell and should not be used in programs.
```

## Imported builtins object

It is possible to get the same list (more or less, please read above) by running:
``` python
for f in [ f for f in dir(__builtins__) if not f.startswith("_") ]: print(f)
```

- `ArithmeticError`
- `AssertionError`
- `AttributeError`
- `BaseException`
- `BaseExceptionGroup`
- `BlockingIOError`
- `BrokenPipeError`
- `BufferError`
- `BytesWarning`
- `ChildProcessError`
- `ConnectionAbortedError`
- `ConnectionError`
- `ConnectionRefusedError`
- `ConnectionResetError`
- `DeprecationWarning`
- `EOFError`
- `Ellipsis`
- `EncodingWarning`
- `EnvironmentError`
- `Exception`
- `ExceptionGroup`
- `False`
- `FileExistsError`
- `FileNotFoundError`
- `FloatingPointError`
- `FutureWarning`
- `GeneratorExit`
- `IOError`
- `ImportError`
- `ImportWarning`
- `IndentationError`
- `IndexError`
- `InterruptedError`
- `IsADirectoryError`
- `KeyError`
- `KeyboardInterrupt`
- `LookupError`
- `MemoryError`
- `ModuleNotFoundError`
- `NameError`
- `None`
- `NotADirectoryError`
- `NotImplemented`
- `NotImplementedError`
- `OSError`
- `OverflowError`
- `PendingDeprecationWarning`
- `PermissionError`
- `ProcessLookupError`
- `RecursionError`
- `ReferenceError`
- `ResourceWarning`
- `RuntimeError`
- `RuntimeWarning`
- `StopAsyncIteration`
- `StopIteration`
- `SyntaxError`
- `SyntaxWarning`
- `SystemError`
- `SystemExit`
- `TabError`
- `TimeoutError`
- `True`
- `TypeError`
- `UnboundLocalError`
- `UnicodeDecodeError`
- `UnicodeEncodeError`
- `UnicodeError`
- `UnicodeTranslateError`
- `UnicodeWarning`
- `UserWarning`
- `ValueError`
- `Warning`
- `ZeroDivisionError`
- `abs`
- `aiter`
- `all`
- `anext`
- `any`
- `ascii`
- `bin`
- `bool`
- `breakpoint`
- `bytearray`
- `bytes`
- `callable`
- `chr`
- `classmethod`
- `compile`
- `complex`
- `copyright`
- `credits`
- `delattr`
- `dict`
- `dir`
- `divmod`
- `enumerate`
- `eval`
- `exec`
- `exit`
- `filter`
- `float`
- `format`
- `frozenset`
- `getattr`
- `globals`
- `hasattr`
- `hash`
- `help`
- `hex`
- `id`
- `input`
- `int`
- `isinstance`
- `issubclass`
- `iter`
- `len`
- `license`
- `list`
- `locals`
- `map`
- `max`
- `memoryview`
- `min`
- `next`
- `object`
- `oct`
- `open`
- `ord`
- `pow`
- `print`
- `property`
- `quit`
- `range`
- `repr`
- `reversed`
- `round`
- `set`
- `setattr`
- `slice`
- `sorted`
- `staticmethod`
- `str`
- `sum`
- `super`
- `tuple`
- `type`
- `vars`
- `zip`
