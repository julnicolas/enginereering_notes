""" This is not the most convenient way though the safest as
file content is read using a fixed chunk size. """

import logging as log
from sys import argv

name = "somefile.txt"
if len(argv) > 1:
    name = argv[1]

try:
    # Using 1 byte to be sure they are several iterations
    SIZE = 1
    with open(name) as f:
        # Chunk == 0 if EOF is reached
        # The while loop stops if a 0 value
        # is evaluated
        while chunk := f.read(SIZE):
            print(chunk, end="")

except FileNotFoundError:
    log.error(f"file not found '{name}'")
