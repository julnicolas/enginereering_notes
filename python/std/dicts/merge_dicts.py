""" Shows how to merge dictionaries. """
d1, d2 = {"a": 1}, {"b": 2}

# Before python 3.9
print(dict(**d1, **d2))

# Since python 3.9
print(d1 | d2)
