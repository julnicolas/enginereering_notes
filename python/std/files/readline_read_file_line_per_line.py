""" This shows how to read a file line per line in an efficient
way given that lines are not too long!

If lines are suspected to be longs or that the risk does matter
then the only safe alternative is the old read using a bounded
byte size. """

import logging as log
from sys import argv

name = "some_file_name.txt"
# Commodity: provide your file name as CLI arg
if len(argv) > 1:
    name = argv[1]

try:
    with open(name) as f:
        for line in f:
            # Usually lines end by '\n' and print adds another
            print(line, end="")
except FileNotFoundError:
    log.error(f"cannot open {name}, file not found")
