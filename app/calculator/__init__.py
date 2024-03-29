""" Calculator and related classes """
from decimal import Decimal
from typing import Callable, List
from app.calculator.operations import add, subtract, multiply, divide

class Calculation:
    """ Calculation object to represent operations """

    def __init__(self, x: Decimal, y: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        self.x = x
        self.y = y
        self.op = operation

    def perform(self) -> Decimal:
        """ Performs the operation using x and y, returns the result """
        return self.op(self.x, self.y)


class Calculator:
    """ Calculator class """

    @staticmethod
    def _perform_operation(
        x: Decimal,
        y: Decimal,
        op: Callable[[Decimal, Decimal], Decimal]
        ) -> Decimal:
        """ Perform an operation """
        calc = Calculation(x, y, op)
        CalculationHistory.add(calc)
        return calc.perform()

    @staticmethod
    def add(x: Decimal, y: Decimal) -> Decimal:
        """ Add two numbers and return the solution """
        return Calculator._perform_operation(x, y, add)

    @staticmethod
    def subtract(x: Decimal, y: Decimal) -> Decimal:
        """ subtract x from y and return the solution """
        return Calculator._perform_operation(x, y, subtract)

    @staticmethod
    def multiply(x: Decimal, y: Decimal) -> Decimal:
        """ multiply x by y and return the solution """
        return Calculator._perform_operation(x, y, multiply)

    @staticmethod
    def divide(x: Decimal, y: Decimal) -> Decimal:
        """ divide x by y and return the solution """
        return Calculator._perform_operation(x, y, divide)


class CalculationHistory:
    """ A history of the previously performed calculations for a calculator """

    history: List[Calculation] = []

    @classmethod
    def add(cls, calc: Calculation):
        """ Add a calculation to the history """
        cls.history.append(calc)

    @classmethod
    def show(cls) -> List[Calculation]:
        """ Return the history of calculations """
        return cls.history

    @classmethod
    def last(cls) -> Calculation:
        """ Get last calculation """
        return cls.history[-1]

    @classmethod
    def clear(cls) -> List[Calculation]:
        """ Clear all calculations """
        cls.history.clear()
        return cls.history

    @classmethod
    def import_history(cls, history: List[Calculation]):
        """ Import a list of calculations into the current calculation history """
        cls.history += history
        return cls.history
