""" Shows how to implement  operator[]
in python.
"""


class A:
    """we want to support a[i]"""

    def __init__(self):
        self._list = [2, 4, 6, 8]

    def __getitem__(self, key: int) -> int:
        """returns an int because the container is a list[int]"""
        return self._list[key]


class B:
    """we want to support the [i, j] notation.
    We'll only support this notation here. [i] alone
    is not supported.
    """

    def __getitem__(self, key: tuple[int, int]) -> int:
        return key[0] + key[1]


class C:
    """with this class the slice notation is going to be
    supported (only) [i:j].
    """

    def __getitem__(self, key: slice) -> list[int]:
        # In this example a stop bound must be
        # provided. With normal operators,
        # stop is set to len(container) by default.
        if not key.stop:
            raise ValueError("missing slice upper bound")

        start = 0 if not key.start else key.start
        stop = key.stop
        step = 1 if not key.step else key.step

        items = []
        for i in range(start, stop, step):
            items.append(i)
        return items


a = A()
print("a[2] == ", a[2])
# This notation works because the underlying is a container
# and it supports the slice notation.
#
# When using a [i:j] a Slice object is passed (slice(i, j, None))
print("a[1:3] == ", a[1:3])
print("b[i, j] == ", B()[1, 2])
print("c[1:3] == ", C()[1:3])
print("c[:6:2] == ", C()[:6:2])
