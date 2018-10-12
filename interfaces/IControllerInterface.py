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
    def change_title_note(self, id, title):
        pass

    @abc.abstractmethod
    def change_text_note(self, id, text):
        pass

    @abc.abstractmethod
    def change_category_note(self, id, category):
        pass

    @abc.abstractmethod
    def delete_all_notes(self):
        pass

