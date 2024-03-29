""" Command to manage calculator history """
from app import Command
from app.calculator import CalculationHistory

class History(Command):
    """ Adds 'history' command """

    help_string="Manage the calculation history. Usage: history <show|last|clear|import|export>\n"

    def __init__(self):
        super().__init__(command_string="history")

        self.command_options = {
            "show": self._show,
            "last": self._last,
            "clear": self._clear,
            "import": self._import,
            "export": self._export
        }

    def run(self, args:list=None):
        """ When executed the program prints a menu of commands """
        if not args:
            self._show()
        else:
            self.command_options[args[0]]()

    def _show(self):
        print(CalculationHistory.show())

    def _last(self):
        print(CalculationHistory.last())

    def _clear(self):
        CalculationHistory.clear()

    def _import(self):
        print("Importing...")

    def _export(self):
        print("Exporting...")
