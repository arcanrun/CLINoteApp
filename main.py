from model.Model import Model
from model.facade.Facade import Facade
from model.facade.subsystem.NotifyUbuntu import NotifyUbuntu
from model.facade.subsystem.DbTools import DBTools
"""
The structure of the programm is based on https://habr.com/post/139454/
The progarm is made in educational purposes (TDD, SOLID, DesignPatterns, MVC pattern)
"""

if __name__ == '__main__':
    model = Model(Facade(DBTools,NotifyUbuntu()))
    model.note_notify()