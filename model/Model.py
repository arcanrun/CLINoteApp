from model.App.Interfaces.INote import INote

class Model:
    def __init__(self):
        pass

    def create_note(self):
        pass

    def get_all_notes(self):
        return [INote()]

if __name__ == '__main__':
    model = Model()

