import datetime
import sys
#import RPi.GPIO as GPIO
#import pigpio

from PySide6.QtCore import QThreadPool, QTimer
from PySide6.QtWidgets import QApplication, QMainWindow

from logic.DBSetupWorker import DBSetupWorker
from view.ui_test import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.threadpool = QThreadPool()
        self.threadpool.setMaxThreadCount(1)

        self.ui.start.clicked.connect(self.start_timer)
        self.ui.stop.clicked.connect(self.stop_timer)
        self.start_time = None

        self.timer = QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_test)

        db_worker = DBSetupWorker(self)
        db_worker.signals.progress.connect(self.test_wow)
        db_worker.signals.finished.connect(self.db_init_done)
        self.threadpool.start(db_worker)

        #GPIO.setmode(GPIO.BOARD)
        #GPIO.setup(17, GPIO.IN)
        #GPIO.add_event_detect(17, GPIO.RISING, callback=self.test_wow, bouncetime=200)
        #self.pi = pigpio.pi()
        #self.pi.set_mode(17, pigpio.INPUT)
        #self.pi.callback(17, 1, self.test_wow)

        #self.con = sqlite3.connect("test.db")
        #curs = self.con.cursor()
        #curs.execute("CREATE TABLE test(driver, time)")

    def start_timer(self):
        self.timer.start()
        self.start_time = datetime.datetime.now()

    def stop_timer(self):
        self.timer.stop()
        self.update_test()

    def update_test(self):
        elapsed_time = datetime.datetime.now() - self.start_time
        self.ui.testTime.setText(str(elapsed_time))

    def test_wow(self, n):
        print("WOW " + str(n))
        #GPIO.remove_event_detect(channel)

    def db_init_done(self):
        print("Done DB")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
    #GPIO.cleanup()
