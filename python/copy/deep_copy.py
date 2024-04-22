""" Creates a deep copy of an object. """

from copy import deepcopy

l = [1, 2, 3]
print(id(l), l)
l2 = deepcopy(l)
print(id(l2), l2)
