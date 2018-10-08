import unittest
import datetime
from model.facade.Facade import Facade
from model.facade.subsystem.Note import Note
from model.facade.subsystem.ShelveDb import ShelveDb
from model.facade.interfaces.INote import INote
import pdb

class FacadeTest(unittest.TestCase):
    def setUp(self):
        self.facade = Facade(ShelveDb())

    def test_create_note(self):

        text = 'Hello!'
        today = datetime.datetime.now()
        category = 'Fun'
        title = 'HI!'

        self.facade.create_note(text, today, category, title)
        res = self.facade.get_note_by_id(0)

        self.assertIsInstance(res, Note)
        self.assertEqual(res.get_text(), text, 'Hello!')
        self.assertEqual(res.get_date(),today, today)
        self.assertEqual(res.get_category(), category.lower())
        self.assertEqual(res.get_title(), title)

    def test_note_on_change(self):
        text = 'Hello!'
        today = datetime.datetime.now()
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

    def test_on_adding_and_getting_items_from_DB(self):
        text = 'Hello!'
        today = datetime.datetime.now()
        category = 'Fun'
        title = 'HI!'
        self.facade.create_note(text, today, category, title)

        note_by_id = self.facade.get_note_by_id('0')

        self.assertEqual(note_by_id.get_text(), text)

    def test_get_all_notes(self):
        text = 'Hello!'
        today = datetime.datetime.now()
        category = 'Fun'
        title = 'HI!'
        self.facade.create_note(text, today, category, title)
        self.facade.create_note(text, today, category, title)

        pdb.set_trace()




        self.assertEqual( len( self.facade.get_all_notes() ), 2 )

    def test_clear_all_notes_from_db(self):
        pass

