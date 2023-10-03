""" Reads a symlink, return its path. """
# If the file or directory pointed by the link
# is not a symbolic or hard link an OSError is raised.

from pathlib import PosixPath as Posix

p = Posix("/foo/bar/bob.txt")
if p.is_symlink():
    print(p.readlink())
else:
    print(f"{p.as_posix()} is not a symlink")

