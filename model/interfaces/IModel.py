import abc


class IModel(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def subscribe(self, subscriber):
        pass

    @abc.abstractmethod
    def unsubscribe(self, index):
        pass

    @abc.abstractmethod
    def update_subscribers(self):
        pass