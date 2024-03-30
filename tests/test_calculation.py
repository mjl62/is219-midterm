""" Tests for Calculation class functions """

from app.calculator import Calculation
from app.calculator.operations import add

def test_init():
    """ Ensure values and operation are intialized properly """
    x, y, op = 22, 5, add
    calculation = Calculation(x, y, op)
    assert calculation.x == 22 and calculation.y == 5 and calculation.op is add

def test_op_symbol_conversion():
    """ Tests operation to symbol conversion """
    assert Calculation.op_to_symbol(add) == "+"

def test_string_op_conversion():
    """ Tests string to operation function conversion """
    assert Calculation.string_to_op("add") is add

def test_perform_op():
    """ Tests that operations can be properly performed """
    x, y, op = 22, 5, add
    calculation = Calculation(x, y, op)
    assert calculation.perform() == 27
