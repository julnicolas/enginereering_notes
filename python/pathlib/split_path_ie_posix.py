""" Split path at the logical level.

For this example, UNIX paths are chosen.
"""
from pathlib import PosixPath

def split_and_print(path: str):
    print(f"input path - {path}")
    p = PosixPath(path)
    print(f"parts - {p.parts}")

split_and_print("foo/bar.zip")
split_and_print("./foo/bar.zip")
split_and_print("./bar.zip")
