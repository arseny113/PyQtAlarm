import sqlite3
from datetime import datetime
import threading
from PyQt5.QtWidgets import QMainWindow, QLabel, QDialog
from PyQt5 import uic
from Alarm import Alarm
from Alarm_info import Info


class UI(QMainWindow):
    is_alarm_available = 0
    ids = []
    listed = []

    closest = None

    def __init__(self):
        super().__init__()
        uic.loadUi('Application.ui', self)
        self.add_alarmButton.clicked.connect(self.create_alarm)

        try:
            self.con = sqlite3.connect('Alarms.db')

            self.is_alarm_available = 1

        except:
            exit()

        self.update_all()

    def setup_alarms(self):
        if self.is_alarm_available == 1:
            self.list_alarms()
            self.datermine_closet_alarms(0)

    def show_time(self):
        time = datetime.now()
        s = ""

        if time.hour < 10:
            s += "0" + str(time.hour)
        else:
            s += str(time.hour)

        s += ":"

        if time.minute < 10:
            s += "0" + str(time.minute)
        else:
            s += str(time.minute)

        s += ":"

        if time.second < 10:
            s += "0" + str(time.second)
        else:
            s += str(time.second)

        self.clockLabel.setText(s)

    def list_alarms(self):
        cur = self.con.cursor()

        data = []
        cur.execute("""SELECT * FROM alarms""")

        for x in cur:
            data.append(x)

        for elem in data:
            if elem[4] not in self.ids:
                label = QLabel(self.tuple_to_string(elem))
                self.list_alarmLayout.addWidget()

                self.listed.append(label)
                self.ids.append(elem[4])

    def tuple_to_string(elem):
        name = elem[0]
        mins = elem[1].minute
        hours = elem[1].hour
        rep = elem[2]
        sound = elem[3].replace("_", " ")

        time = ""
        if (hours < 10):
            time += "0" + str(hours) + ":"
        else:
            time += str(hours) + ":"

        if (mins < 10):
            time += "0" + str(mins)
        else:
            time += str(mins)

        s = time + name + rep + elem[4]

        return s

    def create_alarm(self):
        info_win = Info()
        info_win.exec_()
        self.determine_closet_alarm(0)
        self.list_alarms()

    def determine_closet_alarm(self, state):
        cur = self.con.cursor()
        listed = []

        data = cur.execute("""SELECT * FROM alarms""")
        for x in data:
            if self.closest is None:
                self.closest = Alarm(x[0], x[1], x[2], 3)

            cur = Alarm(x[0], x[1], x[2], 3)

            if state == 5 and cur.is_now():
                continue

            if cur.is_sooner(self.closest) or self.closest.is_now():
                self.closest = cur

    def update_all(self):
        threading.Timer(1.0, self.update_all).start()
        self.show_time()

        if UI.closest is not None and self.closest.is_now():
            temp = self.closest
            self.determine_closest_alarm(5)
            temp.go()
