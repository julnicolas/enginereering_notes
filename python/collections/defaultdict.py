""" Show how to use default dicts. """
from collections import defaultdict

d = defaultdict(lambda: 0)
# Would normally result in a KeyError
d["a"] += 1
d["b"] = 3

for k, v in d.items():
    print(k, v)
