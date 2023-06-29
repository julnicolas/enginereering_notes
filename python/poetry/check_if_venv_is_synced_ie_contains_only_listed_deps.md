# Check if venv is synced
A venv is synced if it only contains dependencies which are listed in the pyproject file.

``` sh
poetry install [--with,--without,--only $GROUP_LIST] --sync
```

`GROUP_LIST` is a comma-separated list of group names
