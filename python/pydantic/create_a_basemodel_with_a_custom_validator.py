""" Pydantic is excelent to validate data structures ensuring attributes'
type hints are respected. It comes along with default validators but custom
ones can be user defined.

It makes it an excellent choice to define well rounded configuration objects.
"""
from pydantic import BaseModel, ValidationError
# Optional if no custom validators are needed!
from pydantic import field_validator, FieldValidationInfo

class NegativePositionError(Exception):
    def __init__(self, *, field: str, value: int):
        super().__init__(f"position {field} is negative with value {value}")

class PositivePosition(BaseModel):
    x: int
    y: int = 0
    z: int = 0

    # Validators are called sequencially on each field
    # They must be class methods
    # FieldValidationInfo is not mandatory
    @field_validator("x", "y", "z")
    @classmethod
    def not_negative(cls, value: int, info: FieldValidationInfo) -> int:
        if value < 0:
            raise NegativePositionError(field=info.field_name, value=value)

        # Must return the value so that it can be set to the class' attribute
        return value

# Now let us instantiate the "struct"
pos = PositivePosition(x=2) # y and z are not needed as defined by default
print(f"OK:\n\t{pos}") 

# x is not defined by default hence mandatory, let us check this
try:
    PositivePosition()
except ValidationError as e:
    print(f"### Validation error:\n\t{e}")

# Now let us check that positions cannot be negative
try:
    PositivePosition(x=-1, y=-2)
except NegativePositionError as e:
    print(f"### Validation error:\n\t{e}")

