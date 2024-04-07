""" Parses an uuid string. Raises an exception
if incorrect.
"""
from uuid import UUID

try:
    UUID("hello")
except ValueError:
    print("value error")
print(UUID("da5c01ba-2628-408b-917e-bfcc05f58a59"))
