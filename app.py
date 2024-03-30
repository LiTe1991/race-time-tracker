"""
    The main application which is used during start proc etc.
"""
import datetime
import sys

from PySide6.QtCore import QThreadPool, QTimer
from PySide6.QtWidgets import QApplication, QMainWindow

import view.RaceView as raceView


class MainWindow(QMainWindow):
    """
        Main Window contain logic for loading race ui and register actions for timer and gpios
    """
    def __init__(self):
        super().__init__()
        self.ui = raceView.Ui_MainWindow()
        self.ui.setupUi(self)

        self.threadpool = QThreadPool()
        self.threadpool.setMaxThreadCount(1)

        self.window = None

        self.ui.actionButton.clicked.connect(self.trigger_timer_action)
        self.start_time = None

        self.timer = QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_test)

    def trigger_timer_action(self):
        """
            Trigger the action for timer, make timer ready or abort proc
        """
        if self.start_time is None:
            self.ui.actionButton.setText("Abbrechen")
            self.timer.start()
            self.start_time = datetime.datetime.now()
        else:
            self.ui.actionButton.setText("Ready")
            self.timer.stop()
            self.start_time = None

    def update_test(self):
        """
            Update the timer label and set actual measured time
        """
        elapsed_time = datetime.datetime.now() - self.start_time
        self.ui.timeLabel.setText(str(elapsed_time))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
