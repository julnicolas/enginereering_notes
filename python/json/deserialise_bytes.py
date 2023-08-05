""" Deserialise a response in bytes in json format. """

import json

response = b'{"msg": "hello"}'

try:
    j = json.loads(response)
except json.JSONDecodeError:
    ...

for k, v in j.items():
    print(f"key == {k}, value == {v}")
