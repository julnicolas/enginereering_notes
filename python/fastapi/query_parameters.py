""" This module shows how to define
query parameters with FastAPI.
"""
from fastapi import FastAPI

app = FastAPI()


@app.get("/item")
async def items(name: str, qty: int = 1, location: str | None = None):
    """Returns an item matching input filters
    :param name str: name of an item, required
    :param qty int: quantity of items, default is 1
    :param location str | None: item's location, optional
        if not provided, any location is considered
    """
    # Not sure how to document str | None type properly
    r = {"name": name, "qty": qty}
    if location:
        r["location"] = location
    return r
