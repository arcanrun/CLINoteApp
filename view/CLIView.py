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

    def main_menu(self):
        print(
"""
1. New note
2. All notes
3. Delete note
4. Find note by...

"""
        )
        n = input()
        dict = {
            '1': self.create_note,
            '2': self.get_all_notes,
            '3': self.delete_note,
            '4': self.menu_find_note
        }
        dict.get(n, self.main_menu)()

    def menu_find_note(self):
        print(
            """
1. Find note by id
2. Find note by category
3. Find note by date
4. Back to main menu
    
            """
        )
        n = input()
        dict = {
            '1': self.get_note_by_id,
            '2': self.get_note_by_category,
            '3': self.get_note_by_date,
            '4': self.main_menu
        }
        dict.get(n, self.main_menu)()

    # controlls methods:

    def delete_note(self):
        print('== WHICH ONE DO YOU WANT TO DELETE? ==')

        self.get_all_notes()
        id = input()
        self.controller.delete_note(id)

        print('ENTER ID NOTE:')

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

        print('Remind? [y/n]')
        choose = input()
        if choose == 'y':
            date_reminder = CLIView.create_date()
            notify = [date_reminder, 0]
        else:
            notify = None

        today = datetime.date.today()

        self.controller.create_note(text, today,  category, title, notify)

    def get_all_notes(self):
        print('== ALL YOUR NOTES ===')
        all_notes = self.model.get_all_notes()
        self.note_view_template(all_notes)

    def get_note_by_id(self):
        self.get_all_notes()
        print('Enter ID: ')
        id = input()

        return self.note_view_template([[id, self.model.get_note_by_id(id)]])

    def get_note_by_category(self):
        self.get_all_notes()
        print('ENTER CATEGORY:')
        category = input()

        notes = self.model.get_notes_by_category(category)
        self.note_view_template(notes) if len(notes) > 1 else self.note_view_template(notes)


    def get_note_by_date(self):
        self.get_all_notes()
        date = self.create_date()

        notes = self.model.get_notes_by_date(date)
        self.note_view_template(notes) if len(notes) > 1 else self.note_view_template(notes)

    def note_view_template(self, all_notes):
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
            border = '.'
            upper_border = border * 15 + '[' + note[0] + ']' + border * 15
            footer_border = len(upper_border) * border

            print('\n')
            print(upper_border)
            print('| Title: ' + title)
            print('| ' + str(date))
            print('| Category: ' + category)
            print('| Remind: ' + str(notification[0]) if notification is not None else None)
            # text = text.split()
            for i in range(0, len(text), len(upper_border)):
                if i % len(upper_border) == 0:
                    text = text[:i] + '\n' + text[i:]
            print(text)
            print(footer_border)


    @staticmethod
    def create_date():
        try:
            print('YEAR')
            y = int(input())

            print('MONTH')
            m = int(input())

            print('DAY')
            d = int(input())

            return datetime.date(y, m, d)
        except:

            CLIView.create_date()


