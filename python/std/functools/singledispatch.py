""" Shows how to use singledispatch
with functions.

To use with methods use
singledispatchmethod
"""
from functools import singledispatch


@singledispatch
def pprint(value: int):
    print(f"printing an int {value}")


@pprint.register
def _(value: float):
    print(f"printing a float {value}")


pprint(1)
pprint(1.0)
