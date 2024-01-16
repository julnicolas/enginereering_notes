""" A dataclass is a class whose attributes are defined
in the class body using type annotations.

Normally when doing so, attributes are shared accross
all instances are they are class attributes. But,
the generated __init__ constructor define them as object
attributes.

Type verification can be done using mypy but no value verification
is carried out. For the latter use pydantic BaseModels.

Dataclasses are very close to structs in C languages in terms of usage.
"""
from dataclasses import dataclass


# kw_only specifies that A can only be instantiated
# by providing explicit attribute names.
# That invalidates filling up the dataclass from a list.
# However parameters can be provided out of order and
# parameter with a default value can be listed before
# parameters without such value.
@dataclass(kw_only=True)
class A:
    x: int = 0
    y: int
    name: str


# Do not trigger an exception as a pydantic.BaseModel would
print(A(y=2, name=3))

# This triggers an exception as attributes with non default values are missing a value
try:
    A()
except TypeError as e:
    print(e)
