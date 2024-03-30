""" Tests for Calculator functionality """
from app.calculator import Calculator

calculator = Calculator()

def test_add():
    """ Tests Calculator.add """
    assert calculator.add(12, 3) == 15

def test_subtract():
    """ Tests Calculator.subtract """
    assert calculator.subtract(12, 3) == 9

def test_multiply():
    """ Tests Calculator.multiply """
    assert calculator.multiply(12, 3) == 36

def test_divide():
    """ Tests Calculator.divide """
    assert calculator.divide(12, 3) == 4
