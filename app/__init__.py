""" Main application class file """

from decimal import Decimal
from dotenv import load_dotenv
from app.cli import CLI, Command
from app.plugins.exit import Exit
from app.plugins.menu import Menu
from app.plugins.add import Add
from app.plugins.history import History


class App:
    """ Main Application Class """
    def __init__(self):
        load_dotenv()
        self.cli = CLI()
        self.load_plugins()

    def load_plugins(self):
        """ Loads all plugins """
        self.cli.register_command(Exit())
        self.cli.register_command(Menu())
        self.cli.register_command(Add())
        self.cli.register_command(History())

    def start(self):
        """ Runs after initialization, handles main program execution """
        self.cli.loop()
