import unittest
from model.Model import Model
from model.facade.Facade import Facade
from model.facade.subsystem.NotifyUbuntu import NotifyUbuntu
from model.facade.subsystem.DbTools import DBTools
import datetime


class TestModel(unittest.TestCase):
    def setUp(self):
        self.db = DBTools()
        self.notifier = NotifyUbuntu()
        self.facade = Facade(self.db, self.notifier)
        self.model = Model(self.facade)

    def test_create_note_from_model(self):
        text = 'I, am note!'
        today = datetime.date.today()
        category = 'Fun'
        title = 'HI!'
        notify = [datetime.date(2015,10,10), 0]

        self.model.create_note(text, today, category, title, notify)
        note = self.model.get_note_by_id('0')

        self.assertEqual(note.text, text)

        self.facade.clear_db()

    def test_gettng_all_notes(self):
        text_1 = 'I, am note!'
        today_1 = datetime.date.today()
        category_1 = 'Fun'
        title_1 = 'HI!'
        notify_1 = [datetime.date(2015, 10, 10), 0]

        self.model.create_note(text_1, today_1, category_1, title_1, notify_1)



        text_2 = 'I, am note!'
        today_2 = datetime.date.today()
        category_2 = 'Fun'
        title_2 = 'HI!'
        notify_2 = [datetime.date(2015, 10, 10), 0]

        self.model.create_note(text_2, today_2,  category_2, title_2, notify_2)


        all_notes = self.model.get_all_notes()

        self.assertEqual(all_notes[0][1].get_text(), text_1)
        self.assertEqual(all_notes[1][1].get_text(), text_2)

        self.facade.clear_db()

    def test_get_notes_by_category(self):
        text_1 = 'I, am note!'
        today_1 = datetime.date.today()
        category_1 = 'Fun'
        title_1 = 'HI!'
        notify_1 = [datetime.date(2015, 10, 10), 0]

        self.model.create_note(text_1, today_1, category_1, title_1, notify_1)

        text_2 = 'I, am note Of common category!'
        today_2 = datetime.date.today()
        category_2 = 'Common'
        title_2 = 'HI!'
        notify_2 = [datetime.date(2013, 2, 10), 0]

        self.model.create_note(text_2, today_2, category_2, title_2, notify_2)

        text_3 = 'I, am note of common category too!'
        today_3 = datetime.date.today()
        category_3 = 'Common'
        title_3 = 'HI!'
        notify_3 = [datetime.date(2016, 10, 10), 0]

        self.model.create_note(text_3, today_3, category_3, title_3, notify_3)

        common_category = self.model.get_notes_by_category('common')

        self.assertEqual(common_category[0][1].get_text(), text_2)
        self.assertEqual(common_category[1][1].get_text(), text_3)

        fun_category = self.model.facade.get_notes_by_category('fun')

        self.assertEqual(fun_category[0][1].get_text(), text_1)

        self.facade.clear_db()

    def test_getting_notes_by_date(self):
        text_1 = 'I, am note!'
        today_1 = datetime.date(2015, 2, 2)
        category_1 = 'Fun'
        title_1 = 'HI!'
        notify_1 = [datetime.date(2015, 2, 2), 0]

        self.model.create_note(text_1, today_1, category_1, title_1, notify_1)

        text_2 = 'I, am note Of common category!'
        today_2 = datetime.date.today()
        category_2 = 'Common'
        title_2 = 'HI!'
        notify_2 = [datetime.date(2016, 11, 30), 0]

        self.model.create_note(text_2, today_2, category_2, title_2, notify_2)

        text_3 = 'I, am note of common category too!'
        today_3 = datetime.date.today()
        category_3 = 'Common'
        title_3 = 'HI!'
        notify_3 = [datetime.date(2016, 11, 30), 0]

        self.model.create_note(text_3, today_3, category_3, title_3, notify_3)



        notes_by_date_1 = self.model.get_notes_by_date(datetime.date(2015, 2, 2))

        self.assertEqual(notes_by_date_1[0][1].get_text(),text_1)


        notes_by_date_today = self.model.get_notes_by_date(datetime.date.today())

        self.assertEqual(notes_by_date_today[0][1].get_text(), text_2)
        self.assertEqual(notes_by_date_today[1][1].get_text(), text_3)

        self.facade.clear_db()

    def test_on_making_read_note(self):
        text_1 = 'I, am note!'
        today_1 = datetime.date(2015, 2, 2)
        category_1 = 'Fun'
        title_1 = 'HI!'

        self.model.create_note(text_1, today_1, title_1, category_1)
        self.model.add_notify('0', datetime.date(2015, 2, 2))

        note = self.model.get_note_by_id('0')

        self.assertEqual(note.get_notification()[1], 0)


        self.model.dont_notify('0')

        note_which_ive_done = self.model.get_note_by_id('0')

        self.assertEqual(note_which_ive_done.get_notification()[1], 1)

        self.facade.clear_db()


    def notificator_on_ubuntu_flash_cards(self):
        text_1 = 'I, am note!'
        today_1 = datetime.date(2015, 2, 2)
        category_1 = 'Fun'
        title_1 = 'HI!'
        notify_1 = [datetime.date(2015, 2, 2), 0]

        self.model.create_note(text_1, today_1,  category_1, title_1, notify_1)

        text_2 = 'I, am note Of common category!'
        today_2 = datetime.date.today()
        category_2 = 'Common'
        title_2 = 'HI!'
        notify_2 = [datetime.date(2016, 11, 30), 0]

        self.model.create_note(text_2, today_2, category_2, title_2, notify_2)

        text_3 = 'I, am note of common category too!'
        today_3 = datetime.date.today()
        category_3 = 'Common'
        title_3 = 'HI!'
        notify_3 = [datetime.date(2016, 11, 30), 0]

        self.model.create_note(text_3, today_3,  category_3, title_3, notify_3)


        self.model.note_notify()

        self.facade.clear_db()


