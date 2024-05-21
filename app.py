"""
    The main application which is used during start proc etc.
"""
import datetime
import sys

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QMainWindow
from gpiozero import MotionSensor, RGBLED

import view.RaceView as raceView


class MainWindow(QMainWindow):
    """
        Main Window contain logic for loading race ui and register actions for timer and gpios
    """
    red_light = (1, 0, 0)
    green_light = (0, 1, 0)
    no_light = (1, 1, 1)

    def __init__(self):
        super().__init__()
        self.ui = raceView.Ui_MainWindow()
        self.ui.setupUi(self)

        self.start_time = None

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_stopwatch_time)

        self.button_is_checked = False
        self.ui.actionButton.setCheckable(True)
        self.ui.actionButton.released.connect(self.trigger_timer_action)
        self.ui.actionButton.setChecked(self.button_is_checked)

        # Set the queue length trigger something like sensitivity
        self.gpio = MotionSensor(22, queue_len=10)
        self.led = RGBLED(red=23, green=24, blue=25, initial_value=self.red_light)

    def trigger_timer_action(self):
        """
            Trigger the action for timer, make timer ready or abort proc
        """
        if self.button_is_checked:
            self.ui.actionButton.setText("Ready")
            self.button_is_checked = False
            self.timer.stop()
            self.led.value = self.red_light
            self.gpio.when_motion = None
        else:
            self.ui.actionButton.setText("Stop")
            self.button_is_checked = True
            self.led.value = self.green_light
            self.gpio.when_motion = self.trigger_start_timer

    def trigger_start_timer(self):
        """
            Trigger the action for timer, make timer ready or abort proc
        """
        self.start_time = datetime.datetime.now()
        print('Start time: ' + str(self.start_time))
        self.led.value = self.no_light
        self.timer.start(100)
        self.gpio.when_motion = self.trigger_stop_timer

    def trigger_stop_timer(self):
        """
            Test
        """
        print('Stop time')
        self.timer.stop()
        self.update_stopwatch_time()

    def update_stopwatch_time(self):
        """
            Update the timer label and set actual measured time
        """
        measured_time = datetime.datetime.now() - self.start_time
        print(str(datetime.datetime.now()) + " " + str(self.start_time))
        print('Update:' + str(measured_time))
        self.ui.timeLabel.setText(str(measured_time))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
