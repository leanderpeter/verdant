from abc import ABC


class BusinessObject(ABC):
    ''' Base class for every business object that owns an ID. 
    business_object is abstract and therefore cant be initialized on its own'''

    def __init__(self):
        self._id = 0

    def set_id(self, aid):
        self._id = aid

    def get_id(self):
        return self._id
