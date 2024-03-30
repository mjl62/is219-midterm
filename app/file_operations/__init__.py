""" File handling functions for application """
import pandas as pd

class FileHandler:
    """ Contains functions for use with csv files """

    @staticmethod
    def read(filename: str):
        """ Read a csv file """
        df = pd.read_csv(filename)
        return df
