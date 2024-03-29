""" Command Line Interface (CLI) Class for user interaction with the application. """
from abc import abstractmethod


class Command:
    """ Command abstract class for plugins to inherit from """
    help_string = None

    """ Command Class for CLI Commands and Plugins """
    def __init__(self, command_string: str):
        self.command_string = command_string

    @abstractmethod
    def run(self, args:list=None):
        """ Function that is called when the command is called through the CLI """


class CLI:
    """ Command Line Interface for the console application """
    def __init__(self):
        self.commands = {}

    def register_command(self, command: Command) -> bool:
        """ Register a new command to the CLI

    Args:
        command_string: A string representing how the command should be called from the command line
        command: A callable representing the method the command should call"""

        self.commands[command.command_string] = command.run
        return True
        ### Pytest HATES general error catching, should figure out a solution in near future
        #try:
        #    self.commands[command_string] = command
        #    return True
        #except Exception as err:
        #    print(f"{err} \nFailed to register a command! This will be in the logs in the future.")
        #    return False


    def loop(self):
        """ CLI Loop, runs for programs lifetime after startup. """
        args = input(">>> ").split()
        user_in = args.pop(0)
        if user_in in self.commands:
            self.commands.get(user_in)(args)
        elif len(user_in) == 0:
            return self.loop()
        else:
            print(f"Unknown command: '{user_in}'")
        return self.loop()

    def help(self):
        """ Prints all currently registered commands """
        print("Commands:")
        for key in self.commands:
            print(f"    {key}")
        print("\n")
