""" Checks if a class implement an interface.
This is called a protocol in python.

Protocols are based on structural typing rather
than nominal typing.

Protocols can also be used to check that a type
has a specific class field. Another note will
be made on this subject.
"""

from typing import Protocol


class Reader(Protocol):
    def read(self, chunk: bytes) -> int: ...


class Buffer:
    def __init__(self, buf: bytes):
        self._buf = buf

    # This method implements the reader interface
    def read(self, chunk: bytes) -> int:
        if self._buf:
            print(chunk)
            return len(chunk)
        return 0


class Parser:
    # using type[] to tell type linter to look for a class object
    # rather than an instance
    def __init__(self, reader: type[Reader] = Buffer):
        self._reader = reader
