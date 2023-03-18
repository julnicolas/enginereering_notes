"""
Gets the current dir.

It maybe more useful if the script changed of directory.
To have a more meaningful result the full path is output
from this script.
"""
from os import path

# Returns . which is useless
print(path.curdir)

# In that case that call is always functional
print(path.realpath(path.curdir))
