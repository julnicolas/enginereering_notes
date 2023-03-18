"""
Returns the full path given a string with special characters,
a relative path or a full path.
"""
from os import path

print(path.realpath('../..'))
