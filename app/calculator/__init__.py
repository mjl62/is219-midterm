""" Calculator and related classes """
from decimal import Decimal
from typing import Callable
from calculator.operations import add, subtract, multiply, divide

class Calculation:
    
    def __init__(self, x: Decimal, y: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        self.x = x
        self.y = y
        self.op = operation
    
    def perform(self) -> Decimal:
        """ Performs the stored operation using x and y, returns solution """
        return self.op(self.x, self.y)
    

class Calculator:
    """ Calculator class """
    
    @staticmethod
    def add(x: Decimal, y: Decimal) -> Decimal:
        """ Add two numbers and return the solution """
        return add(x, y)
    
    @staticmethod
    def subtract(x: Decimal, y: Decimal) -> Decimal:
        """ subtract x from y and return the solution """
        return subtract(x, y)

    @staticmethod
    def multiply(x: Decimal, y: Decimal) -> Decimal:
        """ multiply x by y and return the solution """
        return multiply(x, y)

    @staticmethod
    def divide(x: Decimal, y: Decimal) -> Decimal:
        """ divide x by y and return the solution """
        return divide(x, y)
    

class HistoryManager:
    """ A history of the previously performed calculations for a calculator """
