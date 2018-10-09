from .interfaces.IFacade import IFacade
from .interfaces.INote import INote
from .subsystem.Note import Note


class Facade(IFacade):
    def __init__(self, db=None, notifier=None):
        self.db = db
        self.notifier = notifier

    def set_db(self, db):
        self.db = db

    def create_note(self, text, date, category=None, title=None, notify=None):
        self.db.add(Note(text, date, category, title,))

    def change_note(self, note, id):
        self.db.change_item(note, id)

    def change_text(self, note, new_text):
        note.set_text(new_text)

    def change_category(self, note, new_category):
        note.set_category(new_category)

    def change_title(self, note, new_title):
        note.set_title(new_title)

    def get_note_by_id(self, id):
        return self.db.get_item(id)

    def get_all_notes(self):
        return self.db.get_all_items()

    def delete_note(self, id):
        self.db.delete_item(id)

    def clear_db(self):
        self.db.clear_db()

    def add_notify(self, id, date):
        note = self.get_note_by_id(id)
        note.set_notification(date)
        self.change_note(note, id)

    def check_notification(self):
        self.notifier.notify()

