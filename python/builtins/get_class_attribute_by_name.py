"""Shows how to get a class attribute by name."""


class A:
    def foo_f(self):
        print("called foo_f")

    def foo_g(self):
        print("called foo_g")


a = A()
# Retrieve all methods in a starting by foo_
for f in [a.__getattribute__(f) for f in dir(a) if f.startswith("foo_")]:
    f()
