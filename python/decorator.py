""" Shows how to implement the decorator pattern
in python.

Decorator - function/object calling input function
but transforming its output. It is a function
composition in maths.

Below is a functional implemenation using closures.
"""
from typing import Callable


def printer(f: Callable) -> Callable:
    """Prints function result."""

    # args are provided dynamically
    # restraining them and typing them
    # would be great for stricter scoped
    # decorators
    def inner(*args):
        # Save function in closure data to
        # call later
        result = f(*args)
        print(f"result: {result}\nargs: ", *args)
        return result

    return inner


@printer
def hello(fname: str, lname: str):
    return f"hello {fname} {lname}"


hello("sonic", "the hedgehog")
