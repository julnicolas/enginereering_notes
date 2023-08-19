"""Loads only one yaml document contained in a file."""
import yaml

# for the example, provide a path to a yaml file
from sys import argv, exit
import logging as log

if not len(argv) > 1:
    log.error("missing path to yaml file")
    exit(1)
path = argv[1]

# Open the file then parse its content
with open(path) as f:
    yml = yaml.load_all(f)

# Then the yml file can be accessed as a dict
print(yml)
