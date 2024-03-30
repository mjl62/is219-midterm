""" Tests CalculationHistory functionality """

import pandas as pd
from app.calculator import CalculationHistory, Calculation
from app.calculator.operations import add

def test_show_history():
    """ Tests that history properly appears """
    assert isinstance(CalculationHistory.show(), list)

def test_add_to_history():
    """ Tests adding a calculation to the history """
    CalculationHistory.clear() # Other tests may interfere unless this is done
    calculation = Calculation(12, 2, add)
    assert CalculationHistory.add(calculation) == CalculationHistory.show()

def test_last_history():
    """ Test getting last item from history """
    CalculationHistory.add(Calculation(12, 4, add))
    assert CalculationHistory.last() == CalculationHistory.history[-1]

def test_clear_history():
    """ Ensure history after a clear is empty """
    CalculationHistory.add(Calculation(23, 7, add))
    assert len(CalculationHistory.clear()) == 0

def test_dataframe_list_conversion():
    """ Tests that dataframes can be converted to Calculation lists """
    df = pd.DataFrame([["add", 2, 4], ["subtract", 20, 100]], columns=['op', 'x', 'y'])
    assert isinstance(CalculationHistory.dataframe_to_list(df), list)

def test_import_history():
    """ Test that importing history from .csv functions properly """
    CalculationHistory.clear()
    assert isinstance(CalculationHistory.import_history("tests/data/history.csv")[-1], Calculation)
