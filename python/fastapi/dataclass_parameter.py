""" Shows how to use dataclasses as input route parameters. """
# TODO: Try a pydantic BaseModel

from dataclasses import dataclass

from fastapi import FastAPI


@dataclass
class Item:
    """Returns an item matching input filters
    :param name str: name of an item, required
    :param qty int: quantity of items, default is 1
    :param location str: item's location, optional
        if not provided, any location is considered
    """

    name: str
    qty: int = 1
    location: str | None = None


app = FastAPI()


@app.get("/item")
async def item(e: Item):
    return e
