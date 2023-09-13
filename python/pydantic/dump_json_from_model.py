""" Shows how to convert a pydantic model to a json string. """
from pydantic import BaseModel

class PositivePosition(BaseModel):
    x: int = 1
    y: int = 2
    z: int = 3

p = PositivePosition()
json = p.model_dump_json()

print("json dump's type: ", type(json))
print(f"json document:\n{json}")
