import unittest
from controller.ControllerNote import ControllerNote
from model.Model import Model
from model.facade.Facade import Facade
from model.facade.subsystem.DbTools import DBTools
from model.facade.subsystem.NotifyUbuntu import NotifyUbuntu
import datetime


class ControllerNoteTest(unittest.TestCase):
    def setUp(self):
        self.db = DBTools()
        self.notifier = NotifyUbuntu()
        self.facade = Facade(self.db, self.notifier)
        self.model = Model(self.facade)
        self.controller = ControllerNote(self.model)

    def test_controller_on_creating_notes_and_deleting_all_notes(self):
        text = 'I, am note!'
        today = datetime.date(2015, 2, 2)
        category = 'Fun'
        title = 'HI!'
        notify = [datetime.date(2015, 2, 2), 0]

        self.controller.create_note(text, today, category, title, notify)
        note = self.model.get_note_by_id('0')
        print(note.get_notification())
        self.assertEqual(note.get_title(), title)

        self.controller.delete_all_notes()

    def test_controller_delete_note_by_id(self):
        text = 'I, am note!'
        today = datetime.date(2015, 2, 2)
        category = 'Fun'
        title = 'HI!'
        notify = [datetime.date(2015, 2, 2), 0]

        self.controller.create_note(text, today, category, title, notify)

        text1 = '1'
        today1 = datetime.date(2015, 2, 2)
        category1 = '1'
        title1 = '1!'
        notify1 = [datetime.date(2015, 2, 2), 0]

        self.controller.create_note(text1, today1, category1, title1, notify1)

        text2 = '2'
        today2 = datetime.date(2015, 2, 2)
        category2 = '2'
        title2 = '2'
        notify2 = [datetime.date(2015, 2, 2), 0]

        self.controller.create_note(text2, today2, category2, title2, notify2)


        len_of_db_1 = len(self.model.get_all_notes())


        self.assertEqual(len_of_db_1, 3)

        self.controller.delete_note('2')
        len_of_db_2 = len(self.model.get_all_notes())

        self.assertEqual(len_of_db_2, 2)

        self.controller.delete_all_notes()

