""" This shows how to define keyword-only parameters.

On the first hand positional and keyword parameters are going to be defined.

Then on a second hand how to define keyword-only parameters in python. """

# Definitions
# parameter - name given to an input variable in a function signature
# argument - value passed to a function during a function call. An
#   argument is an instance of a parameter.

# In python they are two ways of providing arguments to a function
# Either by position, that is by respecting parameter order,
# Or by keyword, that is by reusing the parameter name to provide an
# argument value.
# 
# Let us define an example function to explain this.
def hi(name: str, greeting: str = "Hi"):
    print(f"{greeting} {name}!")

# It is possible to call hi like this:
hi("Julien")
hi("Julien", "Hello")
hi("Julien", greeting="Hello")
hi(name="Julien", greeting="Hello")
hi(greeting="Hello", name="Julien")

# On the first 2 calls, python can map parameter value (that is arguments) to
# function arguments because the same position is used as in the function
# definition.
#
# "Julien" and "Hello" are therefore positional arguments for the 'name' and 'greeting'
# parameters.

# In call 3 one positional argument ("Julien") and one keyword
# argument ('greeting="Hello"') are passed to the function

# In call 4, two keyword arguments are used

# In call 5, two keyword arguments are used and on top of it, definition-order is not
# respected. Which shows that keyword arguments allows a function to be called
# without knowing the definition order.

# Though one thing (at least) is common to all these calls - every arguments
# can be passed either by position or by keyword. What if we'd like to impose a
# keyword-only argument passing? There is one way to do so in python:
def hello(name: str, *, greeting: str = "Hello"):
    print(f"{greeting} {name}!")

# Now let's check a few calls
# name is the only argument that can be passed by position
# every other argument after '*' must be passed by keyword only!
# It is possible to ommit 'greeting' here because it has a default value.
hello("Julien")

# This call is invalid because greeting is passed by position whereas
# The use of '*' enforces keyword-only parameter passing
try:
    hello("Julien", "Hi")
except TypeError:
    print("call throws because 'Hi' should have been passed using the parameter keyword")

# This call is valid as 'greeting' is passed by keyword
hello("Julien", greeting="Howdy")

