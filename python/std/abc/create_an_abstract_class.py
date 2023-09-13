""" Shows how to create an abstract class. """
# abc stands for abstract class
from abc import ABC, abstractmethod

class A(ABC):
    # An abstract class cannot be instantiated if it has at least an abstract method.
    # That is, if a class inherits from an abstract class, it can be instantiated if 
    # it doesn't have any abstract method.
    #
    # This is logical in python as overriding an abstract method in a child class is
    # equivalent to shadow the parent class' method.
    @abstractmethod
    def f(self) -> int:
        ...

class B(A):
    def __init__(self):
        super().__init__()

    def f(self) -> int:
        return 1

class C(A):
    def __init__(self):
        super().__init__()

    def f(self) -> int:
        return 2

class D(A):
    ...

try:
    A()
except TypeError:
    print("cannot instantiate A because it is abstract")

print(f"B().f() {B().f()}")
print(f"C().f() {C().f()}")
try:
    D()
except TypeError:
    print("cannot instantiate D because still abstract - f hasn't been 'overriden' (shadowed by D)")

