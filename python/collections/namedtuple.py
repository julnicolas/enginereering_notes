""" Show how to use a namedtuple
Named tuple are mutable contrarly to tuples.
"""

from collections import namedtuple

# Creates a new class object
# It is a subclass of tuple
#
# This creates a class named Point with
# two named fields: x and y.
Point = namedtuple("Point", ["x", "y"])

# Create a new tuple
p = Point(1, 2)
p0 = Point(x=1, y=2)

# From dict
p1 = Point(**{"x": 2, "y": 3})

# Unpack
# using the above it's possible to unpack a dict
x, y = p1

# Convert namedtuple to dict
print(p0._asdict())

# Access fields
print(p0[0], p1.x)

# Generate new tuple from base named tuple
p2 = p0._replace(x=22, y=66)
p2 = p2._replace(y=34)
print(p2)
