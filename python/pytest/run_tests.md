# How to run tests with pytest

Other ways are possible but this layout is simple and functional

```
pkg_name
    __init__.py
    foo.py
    sub_pkg
        __init__.py
        bar.py
tests
    test_foo.py
    sub_pkg
        __init__.py
        test_bar.py
```

Then to run the tests call (from a suitable venv):
``` sh
python -m pytest
```
Note call this from the root of the repository.

## Why python -m pytest rather than pytest alone
Calling `python -m pytest` appends the local directory to the `PYTHON_PATH` making it possible to
import `pkg_name` and `pkg_name.sub_pkg` from test files.

