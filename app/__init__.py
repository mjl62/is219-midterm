""" Main application class file """

import os
import pkgutil
import importlib
import logging
from dotenv import load_dotenv
from app.cli import CLI, Command


class App:
    """ Main Application Class """
    def __init__(self):
        load_dotenv()
        self.logging_setup()
        self.cli = CLI()
        self.load_plugins()
        print(os.environ["MENU"])

    def logging_setup(self):
        """ Set up for logger """
        log_dir = os.environ["LOG_DIR"]
        try:
            os.mkdir(log_dir)
        except FileExistsError:
            pass
        logging.basicConfig(filename=log_dir + "/log.txt", level=logging.INFO,
                            format='%(asctime)s [%(levelname)s] - %(message)s')

    def load_plugins(self):
        """ Loads all plugins from PLUGIN_DIR defined in .env """
        plugin_dir = os.environ["PLUGIN_DIR"]
        plugin_count = 0
        for package in pkgutil.iter_modules([plugin_dir]):
            _, name, ispkg = package
            if ispkg:
                plugin = importlib.import_module(plugin_dir.replace("/", ".") + "." + name)
                for item_name in dir(plugin):
                    item = getattr(plugin, item_name)
                    try:
                        if issubclass(item, (Command, )) and item_name != "Command":
                            self.cli.register_command(item)
                            plugin_count += 1
                    except TypeError:
                        continue # dont attempt to load, but don't raise error
        os.environ["PLUGIN_COUNT"] = str(plugin_count)
        logging.info("Loaded %s plugins successfully", plugin_count)
        os.environ["MENU"] = self.cli.menu
        return True

    def start(self):
        """ Runs after initialization, handles main program execution """
        self.cli.loop()
