# Lint files with Ruff

Rust is a new python linters coded in Rust. It embeds several other linting
and convenience tools to reduce the number of tools to be used in project
to many to nearly one.

## Install
``` sh
pip install ruff
```

## Run ruff in autofix mode
The command below is applied to all files in the current dir, recursively.
```
ruff check --fix .
```

## Run ruff in dry/diff mode
No autfixing is done, returns non 0 code if errors are spotted.
``` sh
ruff check --fix .
```

