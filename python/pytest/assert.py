""" This module shows how to call asserts with pytest """
import pytest

# functions starting by test are executed by pytest
def test_some_asserts():
    """ to run it: pytest assert.py """
    assert 1 == 1
    assert 1 > 0
    assert 1 in [2, 1, 3]
    assert False == True

