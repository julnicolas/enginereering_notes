""" Show how to make a dataclass recursively dict-unpackable.

The technique uses the post_init function. Called after __init__
to tune attribute settings.
"""
from dataclasses import dataclass

@dataclass
class Bar:
    x: int
    y: int

@dataclass
class Foo:
    bars: list[Bar]

    def __post_init__(self):
        if isinstance(self.bars, list) and self.bars:
            self.bars = [ Bar(**bar) for bar in self.bars ]

# Similar to a dictionary decoded from a json or yaml file
bars = [{"x": 1, "y": 2}, {"x": 3, "y": 4}]
foo = Foo(bars)
print(foo)
