import unittest
from model.Model import Model
from model.App.Interfaces.INote import INote

class TestModel(unittest.TestCase):
    def setUp(self):
        self.model = Model()

    def test_on_creating_note_object(self):
        self.model.create_note()

        res = self.model.get_all_notes()

        self.assertEqual(res[0].__class__.__name__, INote().__class__.__name__)