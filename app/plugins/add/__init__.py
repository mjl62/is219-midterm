""" Command for performing addition through the command line """
import sys
from decimal import Decimal, InvalidOperation
from app import Command
from app.calculator import Calculator

class Add(Command):
    """ Adds 'add' command to add numbers """

    help_string = "Add numbers"

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
