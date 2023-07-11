import datetime
import sys
# import RPi.GPIO as GPIO
# import pigpio

from PySide6.QtCore import QThreadPool, QTimer, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QProgressDialog, QPushButton

from logic.DBSetupWorker import DBSetupWorker
from view.ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.threadpool = QThreadPool()
        self.threadpool.setMaxThreadCount(1)

        #self.ui.start.clicked.connect(self.start_timer)
        #self.ui.stop.clicked.connect(self.stop_timer)
        #self.start_time = None

        #self.timer = QTimer()
        #self.timer.setInterval(50)
        #self.timer.timeout.connect(self.update_test)

        self.proc = QProgressDialog("Datenbank wird initialisiert.", "Abbrechen", 0, 100, self)
        close_button = QPushButton('Abbrechen')
        close_button.setEnabled(False)
        self.proc.setWindowTitle(None)
        self.proc.setWindowModality(Qt.WindowModal)
        self.proc.setCancelButton(close_button)
        self.proc.show()

        db_worker = DBSetupWorker(self)
        db_worker.signals.progress.connect(self.db_init_process)
        db_worker.signals.finished.connect(self.db_init_done)
        self.threadpool.start(db_worker)

        # GPIO.setmode(GPIO.BOARD)
        # GPIO.setup(17, GPIO.IN)
        # GPIO.add_event_detect(17, GPIO.RISING, callback=self.test_wow, bouncetime=200)
        # self.pi = pigpio.pi()
        # self.pi.set_mode(17, pigpio.INPUT)
        # self.pi.callback(17, 1, self.test_wow)

        # self.con = sqlite3.connect("test.db")
        # curs = self.con.cursor()
        # curs.execute("CREATE TABLE test(driver, time)")

    #def start_timer(self):
    #    self.timer.start()
    #    self.start_time = datetime.datetime.now()

    #def stop_timer(self):
    #    self.timer.stop()
    #    self.update_test()

    #def update_test(self):
    #    elapsed_time = datetime.datetime.now() - self.start_time
    #    self.ui.testTime.setText(str(elapsed_time))

    def db_init_process(self, n):
        print("Step " + str(n) + " done")
        self.proc.setValue(n)
        # GPIO.remove_event_detect(channel)

    def db_init_done(self, message):
        print(str(message))
        self.proc.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
    # GPIO.cleanup()
