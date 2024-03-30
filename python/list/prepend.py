""" Prepend an element to a list. May resize the list 
with all that it entails. """
# If extra capacity has been allocated by the python runtime
# insert will be able to use it to avoid an extra allocation
l = []
l.insert(0, 1)
print(l)
l.insert(0, 2)
print(l)

# Other way but less efficient as a new list must be allocated,
# then several allocations may occur
# Though that allows to prepend several elements at once
l2 = [3, 4, 5]
l2.extend(l)
print(l2)

# The most efficient solution is to work in a bounded buffer
# and work by shifting values until all space is reached.
# Though that's heavier to code

