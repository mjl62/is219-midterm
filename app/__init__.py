""" Main application class file """

from decimal import Decimal
from app.cli import CLI, Command
from app.plugins.exit import Exit
from app.plugins.menu import Menu


class App:
    """ Main Application Class """
    def __init__(self):
        self.cli = CLI()
        self.load_plugins()

    def load_plugins(self):
        """ Loads all plugins """
        self.cli.register_command(Exit())
        self.cli.register_command(Menu())

    def start(self):
        """ Runs after initialization, handles main program execution """
        self.cli.loop()
