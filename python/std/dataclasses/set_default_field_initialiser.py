""" Sets a default field initialiser. """


import uuid
from dataclasses import dataclass, field


def gen_random_id():
    return uuid.uuid1().hex


@dataclass
class Employee:
    name: str
    id: str = field(default_factory=gen_random_id)
    working_hrs: int = field(default=40)

print(Employee(name="Julien"))
