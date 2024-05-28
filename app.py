"""
    The main application which is used during start proc etc.
"""
import os
import sys

from datetime import datetime, timezone

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QMainWindow
from gpiozero import MotionSensor, RGBLED

from view import RaceView as raceView
from logic import race_timer


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
    rounds_to_drive = 3

    def __init__(self):
        super().__init__()
        self.ui = raceView.Ui_MainWindow()
        self.ui.setupUi(self)

        self.button_is_checked = False
        self.ui.actionButton.setCheckable(True)
        self.ui.actionButton.released.connect(self.trigger_timer_action)
        self.ui.actionButton.setChecked(self.button_is_checked)

        # Updater and Timer
        self.actual_time = None
        self.start_time = None
        self.measured_round_times = []

        self.updater = race_timer.Updater()
        self.updater.worker.update_progress.measured_time.connect(self.update_number)

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

            # TODO: Stop logic to implement
            self.updater.quit()
            self.updater.wait()
            self.start_time = None
            self.actual_time = None
            self.ui.timeLabel.setText('0:00:00:000000')

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
        self.led.value = self.no_light

        self.start_time = datetime.now(timezone.utc)
        self.actual_time = 0

        self.updater.start()

        self.gpio.when_motion = self.take_round_of_finish_race

    def take_round_of_finish_race(self):
        """
            Define the workflow to take round time or stop race.
        """
        if self.actual_time.total_seconds() < 10:
            print("Not yet")
            return

        if len(self.measured_round_times) == (self.rounds_to_drive - 1):
            self.updater.quit()
            self.updater.wait()

        accurate_mode = os.getenv("ACCURATE_MODE", "0")
        if accurate_mode.isdigit() and int(accurate_mode) == 1:
            print('Use ACCURATE_MODE')
            self.update_stopwatch_time(datetime.now(timezone.utc))

        self.measured_round_times.append(self.actual_time)
        self.start_time = datetime.now(timezone.utc)
        self.actual_time = None
        self.ui.timeLabel.setText('0:00:00:000000')

        if len(self.measured_round_times) == (self.rounds_to_drive - 1):
            self.led.value = self.red_light

        print(str(self.measured_round_times))
        # TODO: After stop or in finale round switch light to red

    def update_stopwatch_time(self, time: datetime):
        """
            Update the timer label and set actual measured time
        """
        self.actual_time = time - self.start_time
        self.ui.timeLabel.setText(str(self.actual_time))

    @Slot(datetime)
    def update_number(self, val):
        """
            Slot which receive the signal from timer worker.
        :param val: The measured time.
        """
        self.update_stopwatch_time(val)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
