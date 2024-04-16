# Entry Point Script
To define the entry point, create a main script
with a main function located in `git_repo/pkg_name`.

```
foo/
    pyproject.toml
    foo/
        __init__.py
        app.py
       mod.py 
```
In this example app.py is the main script. It contains
a main function (def main(): ...)

Then in the `pyproject.toml` define:
``` toml
[tool.poetry.scripts]
executable_name = "foo.app:main"
```

After installing the project, users will be able to call
the package using the `executable_name` command.
It is a generated script which calls `foo.app:main`.

