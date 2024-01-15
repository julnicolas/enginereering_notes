""" Shows how to use the raise from syntax.

It allows to keep an ordered list of raised exceptions.
"""
import logging


def raising():
    try:
        raise TypeError("first exception")
    except TypeError as e:
        raise RuntimeError("second exception") from e


try:
    raising()
except RuntimeError:
    # Exception object automatically passed to logging.exception
    logging.exception("give more context here")

print("\n\n### All exceptions have been caught")
