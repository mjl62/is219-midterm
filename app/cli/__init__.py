""" Command Line Interface (CLI) Class for user interaction with the application. """

import os
import logging
from abc import abstractmethod, ABC

class Command(ABC):
    """ Command abstract class for plugins to inherit from """
    help_string = None

    """ Command Class for CLI Commands and Plugins """
    @abstractmethod
    def __init__(self, command_string: str):
        self.command_string = command_string

    @abstractmethod
    def run(self, args:list=None):
        """ Function that is called when the command is called through the CLI """


class CLI:
    """ Command Line Interface for the console application """

    def __init__(self):
        self.commands = {}
        self.menu = "Commands:\n-----------\n"


    def register_command(self, command: Command) -> bool:
        """ Register a new command to the CLI

    Args:
        command: A Command object containing the command to be registered to the CLI """
        command = command()
        self.commands[command.command_string] = command.run
        self.menu += f"{command.command_string} - {command.help_string}\n"
        logging.info("Command Registered: %s", command.command_string)
        return True

    def loop(self):
        """ CLI Loop, runs for programs lifetime after startup. """
        logging.info("CLI started")
        cursor = ">>> "
        try:
            cursor = os.environ["CURSOR"]
            logging.info("Loaded custom cursor: %s", cursor)
        except KeyError:
            pass # Do nothing, don't throw error
        args = input(cursor).split()
        user_in = args.pop(0)
        if user_in in self.commands:
            self.commands.get(user_in)(args)
        elif len(user_in) == 0:
            return self.loop()
        else:
            print(f"Unknown command: '{user_in}'")
        return self.loop()
