""" Shows how to access a parent class' method. Can be useful if one
has already shadowed a base method.
"""
class A:
    def f(self):
        return 0

class B(A):
    # A's constructor doesn't initialise anything so we don't call it!
    # method will be copied over to B at instantiation time.
    #
    # Please note this is for the sake of the example. It is a good
    # practice to call super().__init__() in child classes!
    def f(self):
        print(super().f())
        return 1

print("### A")
print(A().f())

print("### B")
print(B().f())

