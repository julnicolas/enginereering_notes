""" Checks if file at path exists (though it doesn't check the file type) """

from os import path

if path.exists("/home"):
    print("home directory exists")
else:
    print("no home directory found")

