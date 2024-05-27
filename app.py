"""
    The main application which is used during start proc etc.
"""
import datetime
import os
import sys

from PySide6.QtCore import QTimer, Slot
from PySide6.QtWidgets import QApplication, QMainWindow
from gpiozero import MotionSensor, RGBLED

import view.RaceView as raceView
from test import Updater


class MainWindow(QMainWindow):
    """
        Main Window contain logic for loading race ui and register actions for timer and gpios
    """
    red_light = (1, 0, 0)
    green_light = (0, 1, 0)
    no_light = (1, 1, 1)

    button_text_go = "Ready"
    button_text_stop = "Stop"

    measured_round_times = []

    minimal_running_time_seconds = 30

    def __init__(self):
        super().__init__()
        self.ui = raceView.Ui_MainWindow()
        self.ui.setupUi(self)

        #self.timer = QTimer()
        #self.timer.timeout.connect(self.update_stopwatch_time)

        self.button_is_checked = False
        self.ui.actionButton.setCheckable(True)
        self.ui.actionButton.released.connect(self.trigger_timer_action)
        self.ui.actionButton.setChecked(self.button_is_checked)

        # Updater and Timer
        self.actual_time = None
        self.updater = Updater()
        self.updater.worker.update_progress.latest_number.connect(self.update_number)

        # Set the queue length trigger something like sensitivity, value which we can increase to change behavior
        self.gpio = MotionSensor(22, queue_len=10)
        self.led = RGBLED(red=23, green=24, blue=25, initial_value=self.red_light)

    def trigger_timer_action(self):
        """
            Trigger the action for timer, make timer ready or abort proc
        """
        if self.button_is_checked:
            self.ui.actionButton.setText(self.button_text_go)
            self.button_is_checked = False
            #self.timer.stop()
            self.led.value = self.red_light
            self.gpio.when_motion = None
        else:
            self.ui.actionButton.setText(self.button_text_stop)
            self.button_is_checked = True
            self.led.value = self.green_light
            self.gpio.when_motion = self.trigger_start_timer

    def trigger_start_timer(self):
        """
            Trigger the action for timer, make timer ready or abort proc
        """
        #if self.timer.isActive():
        #    return

        #self.start_time = datetime.datetime.now()
        #print('Start time: ' + str(self.start_time))
        self.led.value = self.no_light
        #self.timer.start(100)


        self.updater.start()

        self.gpio.when_motion = self.trigger_stop_timer
        #QTimer.singleShot(self.minimal_running_time_ms, self, self.test)

    def test(self):
        """
            Add action to when_motion event of the motion sensor
        """
        self.gpio.when_motion = self.trigger_stop_timer

    def trigger_stop_timer(self):
        """
            Test
        """
        if self.actual_time.total_seconds() < 10:
            print("Not yeat")
            return
        #if not self.timer.isActive():
        #    return

        print('Stop time')
        #self.timer.stop()

        self.updater.quit()
        self.updater.wait()

        accurate_mode = os.getenv("ACCURATE_MODE", "0")
        if accurate_mode.isdigit() and int(accurate_mode) == 1:
            self.update_stopwatch_time()

    def update_stopwatch_time(self):
        """
            Update the timer label and set actual measured time
        """
        measured_time = datetime.datetime.now(datetime.timezone.utc) - self.updater.worker.start_time
        print('Update:' + str(measured_time))
        self.ui.timeLabel.setText(str(measured_time))

    # Changed pyqtSlot to Slot
    @Slot(datetime.timedelta)
    def update_number(self, val):
        self.actual_time = val
        print("UPDATE NUMBER: ", val)
        self.ui.timeLabel.setText(str(val))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
