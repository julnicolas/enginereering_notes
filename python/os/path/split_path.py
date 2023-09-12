""" Shows how to split a path.

The separator in use is the one used by the system by default.
To generalize this behaviour and handle path at the logical level,
use pathlib instead.
"""
from os import path

p = "./foo/bar.zip"
print(f"input path: {p}")
print(path.split(p))

