from model.facade.interfaces.INotifier import INotifier
import subprocess
# from model.facade.subsystem.ShelveDb import ShelveDb
import shelve


class NotifyUbuntu(INotifier):
    def __init__(self):
        pass
    def notify(self):
        db = shelve.open('ShelveDb')

        for k,v in db:
            notification = v.get_notification
            if (not notification == None) and (not notification[1] == 1):
                #  notify-send -a NoteCLI -i /home/arcan/PycharmProjects/CLINoteApp/icon.png "Title" "text"
                message = '-a NoteCLI -i /home/arcan/PycharmProjects/CLINoteApp/icon.png "Title" "text"'
                subprocess.Popen(['notify-send', message])
        db.close()
        return

if __name__ == '__main__':
    a = NotifyUbuntu()
    print(a.notify())