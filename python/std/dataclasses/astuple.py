""" Converts a dataclass to a tuple. """

from dataclasses import dataclass, astuple


@dataclass
class Point:
    x: int
    y: int


p = Point(1, 2)
t = astuple(p)

assert isinstance(t, tuple)
print(t)
