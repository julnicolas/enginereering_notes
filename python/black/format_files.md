# Format files

Black is good and efficient code formatter. It can format files and rewrite them or simply display
a diff of what's wrong. That way it can either be used by devs or CI pipelines.

## Format files with autofixing formatting issues
This command formats all files recursively in the current dir.
``` sh
black .
```

This command only applies to a restricted set of files:
``` sh
black file1 file2
```

## Issue formatting errors but do not autofix
``` sh
black --diff .
```

