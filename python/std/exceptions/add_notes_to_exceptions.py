""" It is possible to add notes to an exception object.
It is then showed by Exception.__str__.

Availability: Python 3.11
"""

try:
    raise RuntimeError('some error')
except RuntimeError as e:
    e.add_note('this is my custom note')
    print(e)

