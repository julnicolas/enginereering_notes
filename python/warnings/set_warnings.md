# Set Warnings
This document shows the different classes of warnings usable in python.

Warnings are logged to stderr by default, though default processing can be changed to throwing exceptions
by instance.

Other subject related to this, python development modes. This enables to run python with some extra
heavy checks (and more warnings enabled by default) which can be useful for debuging.

## Log a Warning
``` python
import warnings

# leave all warnings to be shown (deprecation warnings are filtered out by default).
# This is not efficient and should not be the default action.
# Some tools such as pytests enable all warnings.
# It can be a good idea to rely on these tools to deal with warning filters.
warnings.simplefilter('always')

# issue a warning
warnings.warn('this is deprecated', DeprecationWarning)
```

## Warning classes
This table was fetched from the python documentation
https://docs.python.org/3/library/warnings.html#warning-categories

## Warning filters
Warning filters must be the subject of another dedicated document.
