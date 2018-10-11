from interfaces.IObserver import IObserver
import datetime


class CLIView(IObserver):
    def __init__(self, model, controller):
        self.model = model
        self.controller = controller
        self.model.subscribe(self)

    # view methods:

    def update(self, data):
        print('== THE NOTES HAS BEEN CHANGED ==')
        self.get_all_notes()

    # controlls methods:

    def delete_note(self):
        self.get_all_notes()
        print('Which one do you want to delete?')
        id = input()
        self.controller.delete_note(id)

    def create_note(self):
        print('Enter the title')
        title = input()
        if title == '':
            self.create_note()

        print('Enter text')
        text = input()
        if text == '':
            self.create_note()

        print('Enter category')
        category = input()
        if category == '':
            category = None

        print('Remind?\n [y/n]')
        choose = input()
        if choose == 'y':
            date_reminder = CLIView.create_date()
            notify = [datetime, 0]
        else:
            notify = None

        today = datetime.date.today()

        self.controller.create_note(text, today, title, category, notify)

    def get_all_notes(self):
        all_notes = self.model.get_all_notes()
        for note in all_notes:

            title = note[1].get_title()
            if title is None:
                title = 'No title'

            category = note[1].get_category()
            if category is None:
                category = 'No category'

            notification = note[1].get_notification()
            if notification is None:
                notification = 'Not given'

            text = note[1].get_text()
            date = note[1].get_date()
            border = '_'
            print('ID: ' + note[0])
            print(border * 50)
            print('=' * 10 + title + '=' * 10)
            print(date)
            print('category: ' + category)
            print('remind: ' + notification)
            print(text)
            print(border * 50)

    @staticmethod
    def create_date():
        try:
            print('Year')
            y = int(input())

            print('Month')
            m = int(input())

            print('Day')
            d = int(input())

            return datetime.date(y, m, d)
        except:

            CLIView.create_date()


