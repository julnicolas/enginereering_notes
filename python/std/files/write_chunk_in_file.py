""" Shows how to write data chunks in files. """
from os import remove
from sys import argv

## Set up stage
name = "foo.txt"
cleanup = True
if len(argv) > 1:
    cleanup = False if argv[1].lower() == "false" else True

## I M P L E M E N T A T I O N
# Open in write mode, replace current content if present, create file
# if it does not exist
with open(name, "w+") as f:
    chunks = ["hello ", "world\n", "hey\n"]
    for c in chunks:
        print(f"writting to {name}: '{c}'")
        f.write(c)

## Cleanup stage
if cleanup:
    print(f"removing {name}")
    remove(name)
