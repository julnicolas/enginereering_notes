""" The assignment expression (aka walrus) operator
enables to label a sub-expression within a broader expression.

The labeling operation described above is an assignment in python
as python is an imperative language.

This feature comes from the functional programming pattern.
"""
# Here are a few examples
import os

# Setting up environments vars for follow up example
os.environ["ENV1"] = "env1 value"
os.environ["ENV2"] = "env2 value"

# The old way without the assignment operator
env1 = os.environ.get("ENV1")
env2 = os.environ.get("ENV2")
if env1 and env2:
    print(f"'{env1}' and '{env1}'")

# With the walrus operator
if (e1 := os.environ.get("ENV1")) and (e2 := os.environ.get("ENV2")):
    print(f"'{e1}' and '{e2}'")
