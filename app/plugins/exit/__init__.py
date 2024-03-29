""" Command for exiting a program through the CLI """
import sys
from app import Command

class Exit(Command):
    """ Adds 'exit' command to stop a running program """

    help_string = "Exits the program"

    def __init__(self):
        super().__init__(command_string="exit")

    def run(self, args:list=None):
        """ Exit the program when the command is executed """
        sys.exit(0)
