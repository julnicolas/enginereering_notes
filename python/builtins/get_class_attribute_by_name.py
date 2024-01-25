"""Shows how to get a class attribute by name.

This is not the standard way of doing it. another note
explains how to use getattr instead. Plus it is to be
reminded that the use of such functions should be reserved
to very specific cases, otherwise the dot notation is the 
one to be preferred.
"""


class A:
    def foo_f(self):
        print("called foo_f")

    def foo_g(self):
        print("called foo_g")


a = A()
# Retrieve all methods in a starting by foo_
for f in [a.__getattribute__(f) for f in dir(a) if f.startswith("foo_")]:
    f()
