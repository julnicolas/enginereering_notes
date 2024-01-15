""" Polymorphism - do a dynamic_cast 
Type checkers such as mypy get confused when functions
return a Base type in the prototype but a covarient type
is actually returned.

In terms of OOP this is sound as respecting the Liskov
substitution principle.

Here is how to address the issue, with almost no runtime impact
(the call is an empty function) without ignoring the error.
"""
from typing import cast


class A:
    ...


class B(A):
    ...


def f() -> A:
    return B()


# Uncomment to see the error from mypy
#b: B = f()

b: B = cast(B, f())
