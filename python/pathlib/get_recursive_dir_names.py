""" Get a list of dirnames from the current path """
from pathlib import PosixPath as Posix

print("path to file")
p = Posix("/foo/bar/hey.txt")
print(p.as_posix())

print("\ndirnames:")
for q in p.parents:
    print(q.as_posix())


