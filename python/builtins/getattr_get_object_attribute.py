""" Gets an object attribute by name. """
import logging as log


class A:
    def __init__(self):
        self.hey = "hey value"


a = A()
print(getattr(a, "hey"), "\n")
try:
    getattr(a, "hello")
except AttributeError as e:
    log.exception(e)

print("\n", getattr(a, "salut", "default value if attribute is not found"))
