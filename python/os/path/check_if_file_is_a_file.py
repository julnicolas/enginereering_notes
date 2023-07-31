""" Check if file at path is a file """

from os import path

if path.isdir("/blah"):
    print("/blah is a file")
else:
    print("/blah doesn't exist or is not a file")
