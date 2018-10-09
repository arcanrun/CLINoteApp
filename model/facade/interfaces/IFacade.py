import abc


class IFacade(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def set_db(self, db):
        pass

    @abc.abstractmethod
    def create_note(self, text, date, category=None, title=None):
        pass

    @abc.abstractmethod
    def change_text(self, note, new_text):
        pass

    @abc.abstractmethod
    def change_category(self, note, new_category):
        pass

    @abc.abstractmethod
    def change_title(self, note, new_title):
        pass

    @abc.abstractmethod
    def get_note_by_id(self, id):
        pass

    @abc.abstractmethod
    def get_all_notes(self):
        pass

    @abc.abstractmethod
    def delete_note(self, id):
        pass

    @abc.abstractmethod
    def clear_db(self):
        pass

    @abc.abstractmethod
    def add_notify(self, item, date):
        pass

    @abc.abstractmethod
    def check_notification(self):
        pass

    @abc.abstractmethod
    def change_note(self, note, id):
        pass

