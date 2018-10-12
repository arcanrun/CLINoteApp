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

    def notify(self):
        db = shelve.open('shelveDb')
        res = [len(db.items())]
        for k, v in db.items():
            res.append(v)
            notification = v.get_notification()
            # print(k, v.get_notification())
            if not(notification is None) and not(notification[1] == 1) and (notification[0] <= datetime.date.today()):
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