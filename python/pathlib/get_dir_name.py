""" Get dirname such as with the dirname command. """
from pathlib import PosixPath as Posix

print("path to file")
p = Posix("/foo/bar/hey.txt")
print(p.as_posix())

print("\ndirname")
p = p.parent
print(p.as_posix())

