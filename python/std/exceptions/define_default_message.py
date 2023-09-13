""" Shows how to define a default message for a custom exception. 

    Note: call e.__str__() to show an exception's message. 
"""


class MyExcept(Exception):
    def __init__(self, msg: str = "", *, foo: str = ""):
        """ Here msg is optional and can be provided as usual (first position).
            then foo must be provided by name only.
        """
        default_msg = "this is my exception"
        msg = msg if msg != "" else default_msg
        
        if foo != "":
            msg += f" - foo: {foo}"

        # Now init the base class with the message
        super().__init__(msg)

print("### Default message")
try:
    raise MyExcept()
except MyExcept as e:
    print(f"exception content:\n\t{e}")

print("### Custom message")
try:
    raise MyExcept("hello")
except MyExcept as e:
    print(f"exception content:\n\t{e}")

print("### Name only argument")
try:
    raise MyExcept(foo="this is foo")
except MyExcept as e:
    print(f"exception content:\n\t{e}")

print("### Error trying to pass foo as positional arg")
try:
    raise MyExcept("custom msg", "this is foo")
except TypeError as e:
    print("!!! This is a TypeError exception because of bad initialisation")
    print(f"exception content:\n\t{e}")

