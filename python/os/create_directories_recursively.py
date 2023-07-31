""" The following command creates directories recursively like
mkdir -p """

import os

try:
    path = "/home/julien/tmp"
    os.makedirs(path)
    print(f"created dir {path}")
except FileExistsError:
    print("file already exists")
