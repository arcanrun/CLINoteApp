from model.interfaces.IModel import IModel


class Model(IModel):
    def __init__(self, facade):
        self.facade = facade
        self.observers = []

    def subscribe(self, subscriber):
        self.observers.append(subscriber)

    def unsubscribe(self, index):
        self.observers.pop(index)

    def update_subscribers(self):
        for sub in self.observers:
            sub.update(self)

    def create_note(self, text, today, category=None, title=None, notify=None):
        self.facade.create_note(text, today, category, title, notify)
        self.update_subscribers() # notify about creation note

    def add_notify(self, id, date):
        self.facade.add_notify(id, date)
        self.update_subscribers()  # notify about adding notification to the note

    def dont_notify(self, id):
        self.facade.change_status_of_note(id, 1)
        self.update_subscribers() # notify that you have done this task

    def get_note_by_id(self, id):
        note = self.facade.get_note_by_id(id)
        return note

    def get_all_notes(self):
        return self.facade.get_all_notes()

    def get_notes_by_date(self, date):
        return self.facade.get_notes_by_date(date)

    def get_notes_by_category(self, category):
        return self.facade.get_notes_by_category(category)

    def note_notify(self):
        return self.facade.check_notification()

    def delete_all_notes(self):
        self.facade.clear_db()
        self.update_subscribers()

    def delete_note(self, id):
        self.facade.delete_note(id)
        self.update_subscribers()






if __name__ == '__main__':
    model = Model()

