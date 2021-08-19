from abc import ABC


class Ticker(ABC):
    '''Base class for every business object that owns some kind of ticker symbol
    '''

    def __init__(self):
        self._ticker = None

    def set_ticker(self, aticker):
        self._ticker = aticker

    def get_ticker(self):
        return self._ticker
