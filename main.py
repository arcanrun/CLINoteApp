from view.CLIView import CLIView
from model.Model import Model
from controller.ControllerNote import ControllerNote

from model.facade.Facade import Facade
from model.facade.subsystem.DbTools import DBTools
from model.facade.subsystem.NotifyUbuntu import NotifyUbuntu


"""
The structure of the programm is based on https://habr.com/post/139454/
The progarm is made in educational purposes (TDD, SOLID, DesignPatterns, MVC pattern)
"""
def app(view):
    view.main_menu()
    app(view)

if __name__ == '__main__':

    db = DBTools()
    notify = NotifyUbuntu()
    facade = Facade(db, notify)

    model = Model(facade)
    controller = ControllerNote(model)
    view = CLIView(model, controller)

    app(view)



