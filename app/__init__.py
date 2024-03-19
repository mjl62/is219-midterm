""" Main application class file """

from decimal import Decimal

class CLI:
    """ Command Line Interface for the console application """
    def __init__(self, commands: dict):
        self.commands = commands

    def register_command(self, command_string: str, command: callable) -> bool:
        """ Register a new command to the CLI

    Args:
        command_string: A string representing how the command should be called from the command line
        command: A callable representing the method the command should call"""

        self.commands[command_string] = command
        return True
        ### Pytest HATES general error catching, should figure out a solution in near future
        #try:
        #    self.commands[command_string] = command
        #    return True
        #except Exception as err:
        #    print(f"{err} \nFailed to register a command! This will be in the logs in the future.")
        #    return False


    def run(self):
        """ CLI Loop, runs for programs lifetime after startup. """
        user_in = input(">>> ")
        if user_in in self.commands:
            self.commands.get(user_in)()
        elif len(user_in) == 0:
            return self.run()
        else:
            print(f"Unknown command: '{user_in}'")
        return self.run()

    def help(self):
        """ Prints all currently registered commands """
        print("Commands:")
        for key in self.commands.keys():
            print(f"    {key}")
        print("\n")


class App:
    """ Main Application Class """
    def __init__(self):
        self.cli = CLI({"exit": exit})
        self.cli.register_command("help", self.cli.help)

    def start(self):
        """ Runs after initialization, handles main program execution """
        self.cli.run()
