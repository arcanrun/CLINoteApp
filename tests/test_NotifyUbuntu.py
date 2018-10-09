import unittest
import subprocess



class NotifyUbuntuTest:
    def setUp(self):
        pass

    def tetst_flash_notifications(self):
        self.sendmessage('HI')

    def sendmessage(self, message):
        subprocess.Popen(['notify-send', message])
        return

if __name__ == '__main__':
    noty = NotifyUbuntuTest()
    noty.sendmessage('Hello!')