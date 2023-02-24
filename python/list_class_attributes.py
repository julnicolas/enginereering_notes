"""
Shows how to print class attributes 
"""
from typing import Any

def print_all(o: Any) -> None:
    """ Prints all attributes of object o """
    for a in o.__dir__(): print(a)

def print_public(o: Any) -> None:
    """ Prints all public attributes of object o """
    o = ''
    for a in filter(lambda a: not a.startswith('_'), o.__dir__()): print(a)

#print_all('')
print_public('')
