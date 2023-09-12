""" Returns a file name's extension in an OS agnostic way. """
from pathlib import PosixPath

print(PosixPath("foo/bar.zip").suffix)
