""" Returns the name of the calling function """
import inspect

def f():
    print(f" caller is '{inspect.stack()[1].function}'")

def g():
    f()

g()
