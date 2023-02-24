""" Shows how to implement a static method.

Static methods are functions. They are bound to their class and copied to
object instances. They do not take the class nor the instance as parameter.

They behave like functions but are present in the class namespace.

Equivalent behaviour can be implemented as a stand alone function...
and maybe that would be more logical that way?
"""

class Greeting:
    @staticmethod
    def hey():
        print('hey')

Greeting.hey() # prints hey
polite_person = Greeting()
polite_person.hey() # prints hey
