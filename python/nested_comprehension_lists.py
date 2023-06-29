"""
Lists all python files recursively from input dir.

It uses a nested comprehension list to do so.

The logic can be used for any comprehension expression.
"""

from os import walk
from sys import argv, exit

if len(argv) != 2:
    print("missing path or too many args")
    exit(1)

working_dir = argv[1]

print(
    "\n".join(
        [
            ": ".join((path, f))
            for path, _, files in walk(working_dir)
            for f in files
            if f.endswith(".py")
        ]
    )
)
