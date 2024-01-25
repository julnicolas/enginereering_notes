""" Shows how to call the reduce function. """
from functools import reduce
import logging as log

# Here a list is used but that can be any iterable
print("sum is ", reduce(lambda x, y: x + y, [1, 2, 3, 4]))
print("sum is ", reduce(lambda x, y: x + y, [1]))

try:
    print("sum is ", reduce(lambda x, y: x + y, []))
except TypeError as e:
    log.error(f"list is empty - {e}")

# Use an initial value as very first argument
# it is placed before the elements of the list
print("sum is ", reduce(lambda x, y: x + y, [], 34))
