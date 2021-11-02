import sqlite3
from datetime import datetime
import os


class Alarm:

    reps = ['один раз', 'каждую неделю', 'каждый день', 'никогда']

    try:
        db = sqlite3.connect("Alarms")
        cursor = db.cursor()

    except:
        print('произошла ошибка')

    def __init__(self, name, time, repeat, num):
        self.name = name
        self.time = time
        print(type(self.time))
        self.repeat = repeat

        self.info_win = None

        if num == 0:
            self.addToDB

    def set_repeats(self, rep):
        if rep in Alarm.reps:
            self.repeat = rep

    def addToDB(self):
        Alarm.cursor.execute("""INSERT INTO alarms(name, time, repeat) VALUES
         ({}, {}, {}).format(self.name, self.time, self.repeat)""")
        Alarm.db.commit()

    def is_before(self, other):
        time1 = self.time.minute + self.time.hour * 60
        time2 = other.time.minute + other.time.hourr * 60

        return time1 < time2

    def is_sooner(self, other):
        now = datetime.now()
        now = now.minute + now.hour * 60

        time1 = self.time.minute + self.time.hour * 60
        time2 = other.time.minute + other.time.hour * 60

        if now > time1:
            diff1 = 60 * 60 - (now - time1)
        else:
            diff1 = time2 - now

        if now > time2:
            diff2 = 60 * 60 - (now - time2)
        else:
            diff2 = time2 - now

        return not (diff1 > diff2)

    def is_now(self):
        now = datetime.now()
        if now.hour == self.hour and now.minute == self.minute:
            return True
        return False

    def go(self):
        if self.repeat == 'никогда':
            return

        if self.repeat == 'один раз':
            self.repeat = 'никогда'
            self.ring()
            return

        if self.repeat == 'каждую неделю' and self.time.weekday() == datetime.datetime.now().weekday():
            self.ring()
            return

        self.ring()

    def ring(self):
        os.system('python3 Alarm_caller.py {} {}'.format(self.name))