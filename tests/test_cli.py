""" Tests for the Command Line Interface and Commands """

import pytest
from app.cli import CLI, Command
from app.plugins import menu

def test_cli():
    """ Test that the CLI properly initializes """
    assert CLI()

def test_register_command():
    """ Test that commands register properly """
    assert CLI().register_command(menu.Menu) is True

def test_command():
    """ Tests that Command can not be directly initialized """
    with pytest.raises(TypeError):
        Command("test") # pylint: disable=abstract-class-instantiated
