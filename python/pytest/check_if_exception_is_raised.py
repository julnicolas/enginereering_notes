""" Checks if an exception has been raised. """

import pytest


def raise_value_error():
    raise ValueError("hello")


def test_raise():
    with pytest.raises(ValueError):
        raise_value_error()
