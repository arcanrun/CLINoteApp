import abc


class INotifier(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def notify(self):
        pass



