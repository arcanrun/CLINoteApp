from interfaces.IControllerInterface import IControllerInterface


class ControllerNote(IControllerInterface):
    def __init__(self, model):
        self.model = model

    def create_note(self, text, today, category, title, notify):
        self.model.create_note(text, today, category, title, notify)

    def set_notification(self):
        pass

    def delete_note(self, id):
        self.model.delete_note(id)

    def change_note(self):
        pass

    def delete_all_notes(self):
        self.model.delete_all_notes()





