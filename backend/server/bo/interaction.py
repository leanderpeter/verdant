from server.bo.ticker_bo import Ticker
from server.bo.uuid_bo import Uuid
from server.bo.business_object import BusinessObject


class Interaction(BusinessObject, Ticker, Uuid):
    def __init__(self):
        self._interaction_name = None

    def set_interaction_name(self, aname):
        self._interaction_name = aname

    def get_interaction_name(self):
        return self._interaction_name

    def __str__(self, ):
        pass

    @staticmethod
    def from_dict(dictionary=dict()):
        obj = Interaction()
        obj.set_id(dictionary['id'])
        obj.set_uuid(dictionary['uuid'])
        obj.set_ticker(dictionary['ticker'])
        obj.set_interaction_name(dictionary['interaction_name'])
        return obj
