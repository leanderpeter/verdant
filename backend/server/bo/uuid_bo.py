from abc import ABC, abstractmethod
import uuid


class Uuid(ABC):
    def __init__(self):
        self._uuid = None

    def set_uuid(self, auuid):
        self._uuid = auuid

    def get_uuid(self):
        return self._uuid

    def create_uuid(self):
        self._uuid = uuid.uuid4()
        return self._uuid
