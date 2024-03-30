""" Command to get a menu of all possible commands """
import os
from app import Command

class Menu(Command):
    """ Adds 'menu' command """

    help_string="Gets a menu of all currently loaded commands"

    def __init__(self):
        super().__init__(command_string="menu")

    def run(self, args:list=None):
        """ When executed the program prints a menu of commands """
        print(os.environ["MENU"])
