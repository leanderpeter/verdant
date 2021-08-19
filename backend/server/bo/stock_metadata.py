from server.bo.ticker_bo import Ticker
from server.bo.uuid_bo import Uuid
from server.bo.business_object import BusinessObject


class StockMetadata(BusinessObject, Ticker):
    def __init__(self):
        self._average_rating = None
        self._marcet_cap = None
        self._average_volume = None
        self._country_code = None
        self._industry = None
        self._sector = None
        self._employees = None
        self._overall_risk = None

    def set_average_rating(self, value):
        self._average_rating = value

    def get_average_rating(self):
        return self._average_rating

    def set_marcet_cap(self, value):
        self._marcet_cap = value

    def get_marcet_cap(self):
        return self._marcet_cap

    def set_average_volume(self, value):
        self._average_volume = value

    def get_average_volume(self):
        return self._average_volume

    def set_country_code(self, value):
        self._country_code = value

    def get_country_code(self):
        return self._country_code

    def set_industry(self, value):
        self._industry = value

    def get_industry(self):
        return self._industry

    def set_sector(self, value):
        self._sector = value

    def get_sector(self):
        return self._sector

    def set_employees(self, value):
        self._employees = value

    def get_employees(self):
        return self._employees

    def set_overall_risk(self, value):
        self._overall_risk = value

    def get_overall_risk(self):
        return self._overall_risk
