import sys
from datetime import datetime
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from Alarm import Alarm
import os


class Info(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('Dialog.ui', self)
        self.repBox.addItems(Alarm.reps)
        self.okButton.clicked.connect(self.add_alarm)
        self.cancelButton.clicked.connect(exit)

    def add_alarm(self):
        name = self.nameEdit.text()
        mins = int(self.minutesSpin.value())
        hours = int(self.hoursSpin.value())
        cur = datetime.now()
        time = cur.replace(hour=hours, minute=mins)
        rep = Alarm.reps[self.repBox.currentIndex()]

        new = Alarm(name, time, rep, 0)

        self.close()
