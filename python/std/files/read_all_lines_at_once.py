""" Shows how to read all lines at once and store them in a list.

This is potentially dangerous as the list can take a lot of RAM!
"""
import logging as log
from sys import argv

name = "somefile.txt"
if len(argv) > 1:
    name = argv[1]

try:
    with open(name) as f:
        print("".join(f.readlines()))
except FileNotFoundError:
    log.error(f"file {name} not found")
