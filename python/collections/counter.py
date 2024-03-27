""" Shows how to use a counter object. """
from collections import Counter

words = ["hello", "hi", "bonjour", "hello"]
print(Counter(words).most_common())
