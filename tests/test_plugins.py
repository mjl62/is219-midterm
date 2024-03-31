""" Tests for the application plugins """
import pytest
from app.plugins import basic_operations, history, menu
from app.plugins import exit as exit_plugin

def test_add(capsys):
    """ Test the addition plugin """
    basic_operations.Add().run(args=['8', '20'])
    captured = capsys.readouterr()
    assert captured.out.strip() == '28'

def test_noninteger(capsys):
    """ Test error catching from invalid args """
    args = ['8', '20', 'a']
    basic_operations.Add().run(args=args)
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Command only accepts numeric values'.strip()
    basic_operations.Subtract().run(args=args)
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Command only accepts numeric values'.strip()
    basic_operations.Multiply().run(args=args)
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Command only accepts numeric values'.strip()
    basic_operations.Divide().run(args=args)
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Command only accepts numeric values'.strip()

def test_no_args(capsys):
    """ Test what happens when there's no args given """
    # Add
    basic_operations.Add().run()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Requires at least one number following 'add'".strip()
    # Subtract
    basic_operations.Subtract().run()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Requires at least one number following 'subtract'".strip()
    # Multiply
    basic_operations.Multiply().run()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Requires at least one number following 'multiply'".strip()
    # Divide
    basic_operations.Divide().run()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Requires at least one number following 'divide'".strip()

def test_subtract(capsys):
    """ Test the subtraction plugin """
    basic_operations.Subtract().run(args=['10', '22'])
    captured = capsys.readouterr()
    assert captured.out.strip() == '-12'

def test_multiply(capsys):
    """ Test the multiplication plugin """
    basic_operations.Multiply().run(args=['10', '22'])
    captured = capsys.readouterr()
    assert captured.out.strip() == '220'

def test_divide(capsys):
    """ Test the division plugin """
    basic_operations.Divide().run(args=['55', '5'])
    captured = capsys.readouterr()
    assert captured.out.strip() == '11'

def test_exit():
    """ Test that the exit plugin properly exits the program """
    with pytest.raises(SystemExit) as e:
        exit_plugin.Exit().run()
    assert e.type == SystemExit
    assert e.value.code == 0 # Make sure we are exiting with proper exit code

def test_history(capsys):
    """ Test that history plugin properly executes """
    history.History().run()
    captured = capsys.readouterr()
    assert captured.out.strip() == history.History.help_string.strip()

def test_menu():
    """ Test that the menu runs without throwing errors """
    assert menu.Menu().run() is None
