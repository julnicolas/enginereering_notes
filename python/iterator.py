""" They are plenty of ways to make iterator objects
in python. 

An iterator is an object able to iterate over data of
a custom class. Such objects must be able to iterate
over and over on a class content for consistent use
(this is generally what's expected from an iterator
as they are used in for loops).

Co-routines implement the iterator pattern (they are
defined with yield). It is possible to define coroutines
that are iterable over and over for instance if they yield
an iterator result.

Generator expressions create generator which are objects
that can be iterated only once. Then generated resources
are used up. 

A specific kind of iterator is called generators.
"""


# Classic, object oriented yet mostly outdated way of
# defining iterator objects
class A:
    def __init__(self):
        self._list = [1, 2, 3, 4]
        self._it = 0

    def __iter__(self):
        """Mandatory function to initialise
        iterator objects, to iterate over class'
        content.
        """
        # Iterator index must be reinitialised upon new
        # iteration because otherwise end of iteration could
        # have already been reached
        self._it = 0
        # We want this object to be iterable
        return self

    def __next__(self):
        """Mandatory function called to make progress
        on iteration.
        """
        if self._it < len(self._list):
            i = self._it
            self._it += 1
            return self._list[i]

        # The iteration protocol expects this exception to be
        # raised upon iteration completion
        raise StopIteration()


print("old school iterator")
print("call 1")
a = A()
for v in a:
    print(v)
print("call 2")
for v in a:
    print(v)


def f():
    """Now using a co-routine with the yield expression.
    Using yield creates a generator object which are intrasecally
    iterable."""
    # Using yield creates an object with iteration capabilities
    # The above protocol is implemented behind the hood with generated
    # __iter__ and __next__ methods
    #
    # Then iteration need not to be manually reset as when exiting the loop
    # after iteration end, new iteration will enter the loop again.
    # On should be cautious that inner class objects iterated over have a
    # consistent behaviour
    for v in [1, 2, 3, 4]:
        yield v


print("calling co-routine")
print("call 1")
for v in f():
    print(v)
print("call 2")
for v in f():
    print(v)

# Finally let's use a generator expression
print("now using generator expressions")
gen = (x for x in range(5))
print("call 1")
for v in gen:
    print(v)
print("call 2")
for v in gen:
    print(v)
print("generator is used up! create a new one so that iteration is possible")
