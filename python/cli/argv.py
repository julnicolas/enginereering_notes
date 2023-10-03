""" The simplest of all solutions.

Not flexible, standard but good for very few arguments.
"""
from sys import argv, exit

def print_help():
    print("some help")

if len(argv) > 1:
    match argv[1].lower():
        case "-h":
            print_help()
        case "--help":
            print_help()
        case _ as v:
            print(v)
else:
    print("missing positional argument")
    exit(1)
