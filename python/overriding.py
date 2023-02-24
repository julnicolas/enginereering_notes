""" There is no method overriding per se in python. Child class methods
shadow their parent counter parts.

The only way to call a parent method with the same name as a child one
is to reference directly the parent class and call the method from there.

Note: Python doesn't implement polymorphism as it relies on duck-typing
to find out which function to call at run time.
-> see duck_typing.md for further information.
"""

class A:
    def a(self):
        print('A::a()')
class B(A):
    def a(self):
        print('B::a()')
    def ba(self):
        # super must be called as `a` is shadowed by this
        # class' implementation
        super().a()

A().a() # prints A::a()
B().a() # prints B::a()
B().ba() # prints A::a()
