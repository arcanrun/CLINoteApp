from model.facade.interfaces.INotifier import INotifier
import subprocess


class NotifyUbuntu(INotifier):
    def __init__(self, db):
        self.db = db

    def notify(self):
        for k,v in self.db:
            notification = v.get_notification
            if (not notification == None) and (not notification[1] == 1):
                #  notify-send -a NoteCLI -i /home/arcan/PycharmProjects/CLINoteApp/icon.png "Title" "text"
                message = '-a NoteCLI -i /home/arcan/PycharmProjects/CLINoteApp/icon.png "Title" "text"'
                subprocess.Popen(['notify-send', message])
                return

