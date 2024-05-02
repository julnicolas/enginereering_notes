""" Returns a dataclass as a dictionary. """

from dataclasses import dataclass, asdict


@dataclass
class Point:
    x: int
    y: int


p = Point(x=1, y=2)
d = asdict(p)
assert isinstance(d, dict)
print(d)
