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

    @abc.abstractmethod
    def delete_item(selfm, id):
        pass

    @abc.abstractmethod
    def clear_db(self):
        pass

    @abc.abstractmethod
    def change_item(self, item, id):
        pass
