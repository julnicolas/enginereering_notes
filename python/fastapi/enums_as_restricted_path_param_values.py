"""
Shows how to use enums to restrict path parameters
to a limited set of well known values.
"""

import logging as log
from enum import StrEnum

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"msg": "hello"}


class Names(StrEnum):
    sonic = "sonic"
    tails = "tails"


# Any other names than present in Names
# Will return a 422 error
@app.get("/name/{fixed_name}")
def name(fixed_name: Names):
    match fixed_name:
        case "sonic":
            return {"msg": "I'm Sonic the Hedgehog"}
        case "tails":
            return {"msg": "Leave it to me!"}


# THIS ROUTE IS NEVER CALLED
# As the path parameter after name/ is already
# evaluated above
@app.get("/name/{fname}")
def name(fname: str):
    return {"msg": f"I am {fname}"}
