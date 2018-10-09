import abc


class INote(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_text(self):
        pass

    @abc.abstractmethod
    def get_category(self):
        pass

    @abc.abstractmethod
    def get_title(self):
        pass

    @abc.abstractmethod
    def get_date(self):
        pass

    @abc.abstractmethod
    def set_text(self, txt):
        pass

    @abc.abstractmethod
    def set_category(self, ctgr):
        pass

    @abc.abstractmethod
    def set_title(self, ttle):
        pass

    @abc.abstractmethod
    def set_date(self, date):
        pass

    @abc.abstractmethod
    def set_notification(self, date):
        pass

    @abc.abstractmethod
    def get_notification(self):
        pass

