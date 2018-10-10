from model.facade.interfaces.INotifier import INotifier
from model.facade.Facade import Facade
from model.facade.subsystem.DbTools import DBTools

import subprocess
import shelve
import datetime


class NotifyUbuntu(INotifier):
    def __init__(self):
        db = DBTools()
        self.facade = Facade(db)

    def create(self):
        text = 'Privet!'
        today = datetime.date.today()
        category = 'Category:Fun'
        title = '4th note!'
        self.facade.create_note(text, today, category, title)
        self.facade.add_notify('3', datetime.date(2019, 10, 10))
        print(self.facade.get_note_by_id('3').get_notification())

    def notify(self):
        db = shelve.open('shelveDb')
        res = [len(db.items())]
        for k, v in db.items():
            res.append(v)
            notification = v.get_notification()
            # print(k, v.get_notification())
            if (not notification is None) and (not notification[1] == '1') and (notification[0] <= datetime.date.today()):
                title = v.get_title()
                category = v.get_category()
                text = '==' + category + '==\n' + v.get_text()
                subprocess.Popen(['notify-send', '-i', '/home/arcan/PycharmProjects/CLINoteApp/icon.png', title, text])
        db.close()
        return res

if __name__ == '__main__':
    a = NotifyUbuntu()
    # a.create()
    print(a.notify())