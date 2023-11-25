""" To annotate that a class is passed rather than an instance, use the type
annotation as follows:
"""


class A:
    def __init__(self):
        self._a = 1


def f(AA: type[A] = A):
    print(AA()._a)


f()
