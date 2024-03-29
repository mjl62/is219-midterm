""" Tests for the operations functions in app/operations """
import pytest
from app.calculator.operations import add, subtract, multiply, divide

def test_add():
    """ Test addition function """
    assert add(4, 6) == 4 + 6

def test_subtract():
    """ Test subtraction function """
    assert subtract(4, 6) == 4 - 6

def test_multiply():
    """ Test multiplication function """
    assert multiply(4, 6) == 4 * 6

def test_divide():
    """ Test division function """
    assert divide(4, 6) == 4 / 6

def test_divide_by_zero():
    """ Test ZeroDivisionError handling """
    with pytest.raises(ValueError):
        divide(4, 0)
