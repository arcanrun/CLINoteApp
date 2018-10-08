from model.facade.interfaces.INote import INote


class Note(INote):
    def __init__(self, text, date, category=None, title=None):
        self.text = text
        self.date = date
        self.category = category.lower()
        self.title = title

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



