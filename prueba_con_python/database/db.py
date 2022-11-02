from abc import ABCMeta, abstractmethod
import pymongo


class Database(metaclass=ABCMeta):
    @abstractmethod
    def insert(self, data, collection_name):
        raise NotImplementedError
