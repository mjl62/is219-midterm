""" Calculator and related classes """
import os
from decimal import Decimal
from typing import Callable, List
import pandas as pd
from app.calculator.operations import add, subtract, multiply, divide
from app.file_operations import FileHandler

class Calculation:
    """ Calculation object to represent operations """

    def __init__(self, x: Decimal, y: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        self.x = x
        self.y = y
        self.op = operation

    def perform(self) -> Decimal:
        """ Performs the operation using x and y, returns the result """
        return self.op(self.x, self.y)

    def __repr__(self):
        return f"{self.x} {Calculation.op_to_symbol(self.op)} {self.y} = {self.perform()}"

    @staticmethod
    def op_to_symbol(operation: Callable[[Decimal, Decimal], Decimal]):
        """ Convert an operation to its mathematical symbol """

        map_operation = {
            add: "+",
            subtract: "-",
            multiply: "x",
            divide: "/"
        }
        return map_operation[operation]

    @staticmethod
    def string_to_op(string: str) -> Callable[[Decimal, Decimal], Decimal]:
        """ Convert a string to a matching operator"""

        map_operation = {
            "add": add,
            "subtract": subtract,
            "multiply": multiply,
            "divide": divide
        }
        return map_operation[string]

    @staticmethod
    def op_to_string(operation: Callable[[Decimal, Decimal], Decimal]) -> str:
        """ Convert a string to a matching operator"""

        map_operation = {
            add: "add",
            subtract: "subtract",
            multiply: "multiply",
            divide: "divide"
        }
        return map_operation[operation]

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
        calc.perform() # see if error gets thrown before adding to history
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
    def add(cls, calc: Calculation) -> List[Calculation]:
        """ Add a calculation to the history """
        cls.history.append(calc)
        return cls.history

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

    @staticmethod
    def dataframe_to_calculations(df: pd.DataFrame) -> List[Calculation]:
        """ Convert a pandas dataframe to a list of Calculations 
        
        Args:
            pandas.DataFrame: A dataframe with the columns 'op', 'x' and 'y'"""
        calc_list: list = []
        for _, row in df.iterrows():
            op = Calculation.string_to_op(row["op"])
            calc_list.append(Calculation(x=row['x'], y=row['y'], operation=op))
        return calc_list

    @classmethod
    def calculations_to_dataframe(cls, calc_list: List[Calculation]) -> pd.DataFrame:
        """ Convert a list of calculations to a dataframe """
        out_list = []
        for item in calc_list:
            out_list.append([Calculation.op_to_string(item.op), item.x, item.y])
        df = pd.DataFrame(out_list, columns=['op', 'x', 'y'])
        return df

    @classmethod
    def import_history(cls) -> List[Calculation]:
        """ Import a list of calculations into the current calculation history """
        try:
            history_dir = os.environ["HISTORY_DIR"] + "/history.csv"
            history = FileHandler.read(filename=history_dir)
            cls.history += CalculationHistory.dataframe_to_calculations(history)
            return cls.history
        except FileNotFoundError:
            print(f"Couldn't find the file '{history_dir}'")
        return cls.history

    @classmethod
    def export_history(cls) -> bool:
        """ Export the history of calculations as a .csv file """
        history_dir = os.environ["HISTORY_DIR"] + "/history.csv"
        df = CalculationHistory.calculations_to_dataframe(cls.history)
        FileHandler.save(df, filename=history_dir)
        return True
