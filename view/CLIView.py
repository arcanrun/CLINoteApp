from interfaces.IObserver import IObserver
import datetime
import sys


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
4. Delete all notes
5. Find note by...
6. Change note
7. Flash reminders
8. Exit

"""
        )
        n = input()
        dict = {
            '1': self.create_note,
            '2': self.get_all_notes,
            '3': self.delete_note,
            '4': self.delte_all_notes,
            '5': self.menu_find_note,
            '6': self.change_note,
            '7': self.flash_notify,
            '8': self.exit_app

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

    def change_note(self):
        print(
            """
1. Change title of note
2. Change text of note
3. Remind me
4. Don't remind me anymore
5. Back to main menu

            """
        )
        n = input()
        dict = {
            '1': self.change_title_note,
            '2': self.change_text_note,
            '3': self.remind_me,
            '4': self.dont_remind_me,
            '5': self.main_menu
        }
        dict.get(n, self.main_menu)()

    # controlls methods:
    def change_title_note(self):
        self.main_menu()

    def change_text_note(self):
        self.main_menu()

    def dont_remind_me(self):
        self.get_all_notes()
        print('ENTER ID: ')
        id = input()
        try:
            self.controller.remove_notification(id)
            self.main_menu()
        except:
            print('ERROR WHILE REMOVING NOTIFICATION')
            self.main_menu()

    def remind_me(self):
        self.get_all_notes()
        print('ENTER ID: ')
        id = input()
        date = CLIView.create_date()
        try:
            self.controller.set_notification(id, date)
            self.main_menu()
        except:
            print('ERROR WHILE SETTING NOTIFICATION')
            self.main_menu()

    def delete_note(self):
        print('== WHICH ONE DO YOU WANT TO DELETE? ==')

        self.get_all_notes()
        print('ENTER ID NOTE:')
        id = input()
        self.controller.delete_note(id)



    def delte_all_notes(self):
        print("DO YOU REALLY WANT TO DELETE ALL YOUR NOTES? [y/n]")
        n = input()
        if not n.lower() == 'y':
            self.main_menu()
        else:
            self.model.delete_all_notes()
            self.main_menu()

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

        notify = CLIView.set_notification()

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
        try:
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
                if not notification is None:
                    if notification[1] == 0:
                        notification = 'will remind at {}'.format(notification[0])
                    else:
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
                print('| Remind: ' + notification if notification is not None else None)
                # text = text.split()
                for i in range(0, len(text), len(upper_border)):
                    if i % len(upper_border) == 0:
                        text = text[:i] + '\n' + text[i:]
                print(text)
                print(footer_border)
        except:
            print("ERROR...")
            self.main_menu()

    def flash_notify(self):
        self.model.note_notify()


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

    @staticmethod
    def set_notification():
        print('Remind? [y/n]')
        choose = input()
        if choose == 'y':
            date_reminder = CLIView.create_date()
            notify = [date_reminder, 0]
        else:
            notify = None
        return notify

    @staticmethod
    def exit_app():
        sys.exit('Bye-bye!')


