""" Command for performing basic operations through the command line """
import sys
from decimal import Decimal, InvalidOperation
from app import Command
from app.calculator import Calculator

class Add(Command):
    """ Adds 'add' command to add numbers """

    help_string = "Add numbers together. Usage: add <value> <value>..."

    def __init__(self):
        super().__init__(command_string="add")

    def run(self, args:list=None):
        try:
            if not args:
                print("Requires at least one number following 'add'")
                return

            args = list(map(Decimal, args)) # Convert to integers
            total = args.pop(0)
            for num in args:
                total = Calculator.add(total, num)
            print(total)
        except InvalidOperation:
            print("Command only accepts numeric values")


class Subtract(Command):
    """ Adds 'subtract' command to subtract numbers """

    help_string = "Subtract numbers from eachother. Usage: subtract <value> <value>..."

    def __init__(self):
        super().__init__(command_string="subtract")

    def run(self, args:list=None):
        try:
            if not args:
                print("Requires at least one number following 'subtract'")
                return

            args = list(map(Decimal, args)) # Convert to integers
            total = args.pop(0)
            for num in args:
                total = Calculator.subtract(total, num)
            print(total)
        except InvalidOperation:
            print("Command only accepts numeric values")


class Multiply(Command):
    """ Adds 'multiply' command to multiply numbers """

    help_string = "Multiply numbers from eachother. Usage: multiply <value> <value>..."

    def __init__(self):
        super().__init__(command_string="multiply")

    def run(self, args:list=None):
        try:
            args = list(map(Decimal, args)) # Convert to integers
            
            if not args[1]: # Throws IndexError if there is not two values
                return
            
            total = args.pop(0)
            for num in args:
                total = Calculator.multiply(total, num)
            print(total)
        except InvalidOperation:
            print("Command only accepts numeric values")
        except IndexError:
                print("Requires at least two numbers following 'multiply'")


class Divide(Command):
    """ Adds 'divide' command to divide numbers """

    help_string = "Divide numbers from eachother. Usage: divide <value> <value>..."

    def __init__(self):
        super().__init__(command_string="divide")

    def run(self, args:list=None):
        try:
            if not args:
                print("Requires at least one number following 'divide'")
                return

            args = list(map(Decimal, args)) # Convert to integers
            total = args.pop(0)
            for num in args:
                total = Calculator.divide(total, num)
            print(total)
        except InvalidOperation:
            print("Command only accepts numeric values")
        except ValueError:
            print("You cannot divide by zero!")