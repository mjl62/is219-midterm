from app.operations import add, subtract, multiply, divide
import pytest

def test_add():
    assert add(4, 6) == 4 + 6

def test_subtract():
    assert subtract(4, 6) == 4 - 6

def test_multiply():
    assert multiply(4, 6) == 4 * 6

def test_divide():
    assert divide(4, 6) == 4 / 6

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(4, 0)