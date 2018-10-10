import unittest
import datetime
from model.facade.Facade import Facade
from model.facade.subsystem.Note import Note
from model.facade.subsystem.ShelveDb import ShelveDb
from unittest.mock import MagicMock
from model.facade.interfaces.INote import INote
import pdb


class FacadeTest(unittest.TestCase):
    def setUp(self):
        db = ShelveDb()
        self.facade = Facade(db)

    def test_create_note_and_delete_note_by_id(self):

        text = 'Hello!'
        today = datetime.date.today()
        category = 'Fun'
        title = 'HI!'
        self.facade.create_note(text, today, category, title)
        res = self.facade.get_note_by_id(0)

        self.assertIsInstance(res, Note)
        self.assertEqual(res.get_text(), text, 'Hello!')
        self.assertEqual(res.get_date(), today)
        self.assertEqual(res.get_category(), category.lower())
        self.assertEqual(res.get_title(), title)

        self.facade.delete_note('0')

    def test_note_on_change_and_clear_db(self):
        text = 'Hello!'
        today = datetime.date.today()
        category = 'Fun'
        title = 'HI!'

        self.facade.create_note(text, today, category, title)
        note = self.facade.get_note_by_id(0)

        new_text = 'Bye-Bye!'
        new_category = 'Buisness'
        new_title = 'Bye!'

        self.facade.change_text(note, new_text)
        self.facade.change_category(note, new_category.lower())
        self.facade.change_title(note, new_title)

        self.assertEqual(note.get_text(), new_text)
        self.assertEqual(note.get_category(), new_category.lower())
        self.assertEqual(note.get_title(), new_title)

        self.facade.clear_db()

    def test_on_adding_and_getting_items_from_DB_and_clear_db(self):
        text = 'Hello!'
        today = datetime.date.today()
        category = 'Fun'
        title = 'HI!'
        self.facade.create_note(text, today, category, title)

        note_by_id = self.facade.get_note_by_id('0')

        self.assertEqual(note_by_id.get_text(), text)

        self.facade.clear_db()

    def test_get_all_notes_and_clear_db(self):
        text = 'Hello!'
        today = datetime.date.today()
        category = 'Fun'
        title = 'HI!'
        self.facade.create_note(text, today, category, title)
        self.facade.create_note(text, today, category, title)

        # pdb.set_trace()

        self.assertEqual( len( self.facade.get_all_notes() ), 2 )

        self.facade.clear_db()

    def test_adding_notification_tag(self):
        text = 'Hello!'
        today = datetime.date.today()
        category = 'Fun'
        title = 'HI!'
        self.facade.create_note(text, today, category, title)
        note = self.facade.get_note_by_id('0')


        note.set_notification(datetime.date(2018, 10, 10))

        self.assertEqual(note.get_notification(), [datetime.date(2018, 10, 10), 0])


        self.facade.add_notify('0', datetime.date(2000, 1, 1))
        note_changed = self.facade.get_note_by_id('0')
        # pdb.set_trace()
        self.assertEqual(note_changed.get_notification(), [datetime.date(2000, 1, 1), 0])

        self.facade.clear_db()

    def test_on_changeble_status_of_notes(self):
        text = 'Hello!'
        today = datetime.date.today()
        category = 'Fun'
        title = 'HI!'
        self.facade.create_note(text, today, category, title)
        self.facade.add_notify('0', datetime.date(2019, 10, 10))
        self.facade.change_status_of_note('0','1')
        changed_status_note = self.facade.get_note_by_id('0')
        print(changed_status_note.get_notification())

        self.assertEqual(changed_status_note.get_notification()[1], '1')

        self.facade.clear_db()





