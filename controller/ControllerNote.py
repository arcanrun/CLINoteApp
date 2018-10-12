from interfaces.IControllerInterface import IControllerInterface


class ControllerNote(IControllerInterface):
    def __init__(self, model):
        self.model = model

    def create_note(self, text, today, category, title, notify=None):
        self.model.create_note(text, today, category, title, notify)

    def set_notification(self, id, date):
        self.model.add_notify(id, date)

    def remove_notification(self, id):
        self.model.dont_notify(id)

    def change_title_note(self, id, new_title):
        self.model.change_title_note(id, new_title)

    def change_text_note(self, id, new_text):
        self.model.change_text_note(id, new_text)

    def change_category_note(self, id, new_category):
        self.model.change_category_note(id, new_category)

    def delete_note(self, id):
        self.model.delete_note(id)

    def delete_all_notes(self):
        self.model.delete_all_notes()





