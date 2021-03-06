from .interfaces.IFacade import IFacade
from .subsystem.Note import Note
import datetime


class Facade(IFacade):
    def __init__(self, db=None, notifier=None):
        self.db = db
        self.notifier = notifier

    def set_db(self, db):
        self.db = db

    def create_note(self, text, date, category=None, title=None, notify=None):
        self.db.add(Note(text, date, category, title, notify))

    def change_note(self, note, id):
        self.db.change_item(note, id)

    def change_text(self, id, new_text):
        note = self.get_note_by_id(id)
        note.set_text(new_text)
        self.change_note(note, id)

    def change_category(self, id, new_category):
        note = self.get_note_by_id(id)
        note.set_category(new_category)
        self.change_note(note, id)

    def change_title(self, id, new_title):
        note = self.get_note_by_id(id)
        note.set_title(new_title)
        self.change_note(note, id)

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
        return self.notifier.notify()

    def change_status_of_note(self, id, status):
        note = self.get_note_by_id(id)
        note.change_status_notification(status)
        self.change_note(note, id)

    def get_notes_by_category(self, category):
        return self.db.get_items_by_category(category)

    def get_notes_by_date(self, date):
        if isinstance(date, datetime.date):
            return self.db.get_items_by_date(date)
        else:
            raise TypeError



