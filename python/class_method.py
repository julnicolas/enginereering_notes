""" Shows how to define a class method -
aka a method for the class itself.

Here we'll be implementing a factory as an example.
Though factories should rather be implemented as 
stand-alone objects. """

class Person:
    def __init__(self, age, hair_color):
        self._age = age
        self._hair_color = hair_color

    @classmethod
    def make_super_sayen(cls, age):
        return cls(age=age, hair_color='yellow')

