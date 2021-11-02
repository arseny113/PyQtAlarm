from PyQt5.QtMultimedia import QSoundEffect
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import sys


class AlarmCaller(QMainWindow):
    def __init__(self, name):
        super().__init__()
        self.name = name
        uic.loadUi('Alarm_Trigger.ui', self)
        self.sound = QSoundEffect()
        self.sound.setSource(QUrl.fromLocalFile('sounds_default.wav'))
        self.ok_button.clicked.connect(self.quit)
#        self.snooze_button

    def quit(self):
        self.close()
        self.sound.stop()
        sys.exit(0)

    def exec_(self):
        self.sound.play()
        self.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    name = ''
    for i in range(2, len(sys.argv) - 1):
        name += sys.argv[i] + " "

    name = name[:-1]

    win = AlarmCaller(name)
    win.exec_()
    sys.exit(app.exec_())