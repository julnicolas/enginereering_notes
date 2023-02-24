"""
Shows various aproaches to filter lists
"""
from typing import List, Callable

def builtin_filter(l: List, pred: Callable[[], bool]) -> List:
    """
    filter content using the builtin filter function.
    It takes a predicate and a list. It returns an iterable.
    """
    return filter(pred, l)

def comprehension_list(l: List, pred: Callable[[], bool]) -> List:
    """
    Filter content using a list comprehension.
    A conditional statement is used to select items.
    """
    return [x for x in l if pred(x)]

for item in builtin_filter([1, 2, 3], lambda x: x > 1): print(item)
#for item in comprehension_list([1, 2, 3], lambda x: x > 1): print(item)
