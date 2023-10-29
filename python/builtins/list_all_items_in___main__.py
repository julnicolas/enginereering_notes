"""List all items in __main__ module."""
# Gotcha: __main__ is not defined, items are stored in another structure.
# __main__ is just a name convention understood by the python interpreter
# to refer to the module directly summoned by the interpreter.

# utility import
from sys import exit


# Defined to show that user function names can be obtained with
# the method below
def some_user_function():
    ...


if __name__ == "__main__":
    print("listing all items in __main__:\n")
    print("\n".join([o for o in dir()]))
else:
    print("error, not running as __main__ module")
    exit(1)
