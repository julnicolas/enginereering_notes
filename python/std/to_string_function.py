""" Shows how to define the to_string function
for any object in a standard way.
"""


class A:
    # this is a class attribute
    x: int = 2

    def __str__(self) -> str:
        return f"A.x = {self.x}"


print(A())
