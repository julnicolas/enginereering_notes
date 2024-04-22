""" Get reference count for object. """

from sys import getrefcount


def count(obj):
    print(getrefcount(obj))  # a new ref is created here


l = []  # the object is created here
count(l)  # a new ref is created here when calling
# hence the result being 3

ll = l
count(l)

# ref count is decremented by explicitely
# calling del or if ref goes out of scop
del ll
count(l)
