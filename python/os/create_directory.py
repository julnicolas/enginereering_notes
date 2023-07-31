""" Creates a single directory. All directories before the last 
path element must exist. """

import os

path = ""

try:
    os.mkdir(path)
    print(f"created dir {path}")
except FileNotFoundError:
    print(f"one of the directories in path '{path}' doesn't exist")
except FileExistsError:
    print("file already exists")
