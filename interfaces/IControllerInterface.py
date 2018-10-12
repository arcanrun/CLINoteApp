import abc


class IControllerInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_note(self, text, today, category, title, notify):
        pass

    @abc.abstractmethod
    def set_notification(self, id, date):
        pass

    @abc.abstractmethod
    def remove_notification(self, id):
        pass

    @abc.abstractmethod
    def delete_note(self, id):
        pass

    @abc.abstractmethod
    def change_note(self):
        pass

    @abc.abstractmethod
    def delete_all_notes(self):
        pass

