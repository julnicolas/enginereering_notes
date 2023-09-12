""" Get file name in a path. """
from pathlib import PosixPath

print(PosixPath("foo/bar.zip").name)
