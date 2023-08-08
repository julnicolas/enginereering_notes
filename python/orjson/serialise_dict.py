"""
Shows how to serialise a dictionary in json.

The orjson package is not from the standard library.
It is implemented in rust.

It is not an exact drop in replacement but  is quite
compatible with the default package.
"""
import logging as log
import sys
from time import time

import orjson

d = {
    "name": "Sonic",
    "job": "go fast",
}

print("serialising dictionary")
try:
    start = time()
    j = orjson.dumps(d)
    end = time()
except JSONEncodeError:
    log.error("couldn't serialise json struct")
    sys.exit(1)

print(j)
print(f"\nserialisation took {end - start} seconds")
