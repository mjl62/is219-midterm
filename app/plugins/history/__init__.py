""" Command to manage calculator history """
from app import Command
from app.calculator import CalculationHistory

class History(Command):
    """ Adds 'history' command """

    help_string="Manage the calculation history. Usage: history <show|last|clear|save|load>\n"

    def __init__(self):
        super().__init__(command_string="history")

        self.command_options = {
            "show": self._show,
            "last": self._last,
            "clear": self._clear,
            "load": self._import,
            "save": self._export
        }

    def run(self, args:list=None):
        """ When executed the program prints a menu of commands """
        if not args:
            print(self.help_string)
        else:
            self.command_options[args[0]](_args=args)

    def _show(self, _args):
        for i in CalculationHistory.show():
            print (i)

    def _last(self, _args):
        print(CalculationHistory.last())

    def _clear(self, _args):
        CalculationHistory.clear()

    def _import(self, _args):
        CalculationHistory.import_history()
        print("Load success!")

    def _export(self, _args):
        if CalculationHistory.export_history():
            print("Save success!")
        else:
            print("Save failed!")
