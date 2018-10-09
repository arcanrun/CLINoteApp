from model.facade.interfaces.INote import INote
import datetime

class Note(INote):
    def __init__(self, text, date, category=None, title=None, notify=None):
        self.text = text
        self.date = date
        self.category = category.lower()
        self.title = title
        self.notify = notify

    def get_text(self):
        return self.text

    def get_category(self):
        return self.category

    def get_title(self):
        return self.title

    def get_date(self):
        return self.date

    def set_text(self, text):
        self.text = text

    def set_category(self, category):
        self.category = category

    def set_title(self, title):
        self.title = title

    def set_date(self, date):
        self.date = date

    def set_notification(self, date):
        if isinstance(date, datetime.date):
            self.notify = [date, 0]
        else:
            raise TypeError

    def get_notification(self):
        return self.notify

