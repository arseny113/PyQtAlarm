from PyQt5.QtWidgets import *
from Alarm_ui import UI
import sys
import sqlite3


try:
    db = sqlite3.connect('alarms.db')

    cursor = db.cursor()
except:
    print("Error connecting to Database. Alarm won't work")


def quit_all():
    print("QUIT ALL")
    sys.exit(0)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


app = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(True)

app.setStyle("Fusion")
win = UI()

sys.excepthook = except_hook
win.show()

ret = app.exec_()
app.quit()
sys.exit(0)