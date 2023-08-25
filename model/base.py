""" This is the base model, upon all others shall be based """
import pandas as pd

class BaseModel:
    """ Base model other models inherit from """
    def __init__(self, data):
        self._data = data
        self._df = None
        self._dtypes = []

    @property
    def data(self):
        """ Just return the data """
        return self._data
    
    @property
    def df(self):
        """ Get a dataframe of the data """
        if not self._df:
            self._df = pd.DataFrame(self._data).astype(self._dtypes)

        return self._df
