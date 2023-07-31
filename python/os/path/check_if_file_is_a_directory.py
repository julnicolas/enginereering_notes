""" Check if file at path is a directory """

from os import path

if path.isdir("/home"):
    print("/home is a directory")
else:
    print("/home doesn't exist or is not a directory")
