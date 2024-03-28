""" Testing the basic application functionality """

from app import App

app = App()

def test_app_startup():
    """ Ensure app is actually instantiated """
    assert app

def dummy_function():
    """ Dummy function for testing command registration """

#def test_register_command():
#    """ Uses dummy function to test command registration """
#    assert app.cli.register_command("test", dummy_function)
