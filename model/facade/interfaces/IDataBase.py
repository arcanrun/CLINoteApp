import abc


class IDataBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def add(self, item):
        pass

    @abc.abstractmethod
    def get_all_items(self):
        pass

    @abc.abstractmethod
    def get_item(self, id):
        pass
