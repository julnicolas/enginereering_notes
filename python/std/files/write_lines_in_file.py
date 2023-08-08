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
    print("writting lines")
    chunks = ["hello ", "world\n", "hey\n"]
    # No line-separators are added by writelines so
    # it must be done in the provided list of lines
    f.writelines(chunks)

## Cleanup stage
if cleanup:
    print(f"removing {name}")
    remove(name)
