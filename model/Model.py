from model.interfaces.IModel import IModel


class Model(IModel):
    def __init__(self, facade):
        self.facade = facade
        self.observers = []

    def subscribe(self, subscriber):
        self.observers.append(subscriber)

    def unsubscribe(self, index):
        self.observers.pop(index)

    def notify_subscribers(self):
        for sub in self.observers:
            sub.update(self)

    def create_note(self, text, today, title=None, category=None, notify=None):
        self.facade.create_note(text, today, category, title, notify)
        self.notify_subscribers()

    def get_note_by_id(self, id):
        note = self.facade.get_note_by_id(id)
        # self.notify_subscribers()
        return note

    def get_all_notes(self):
        return self.facade.get_all_notes()

    def get_notes_by_date(self, date):
        return self.facade.get_notes_by_date(date)

    def get_notes_by_category(self, category):
        return self.facade.get_notes_by_category(category)


if __name__ == '__main__':
    model = Model()

