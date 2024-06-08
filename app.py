"""
    The main application which is used during start proc etc.
"""
import os
import sys

from datetime import datetime, timezone

from PySide6.QtCore import Slot
from PySide6.QtGui import QTextFormat
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from gpiozero import MotionSensor, RGBLED

from view import RaceView as raceView
from logic import race_timer
from dto import constants


class MainWindow(QMainWindow):
    """
    Main Window contain logic for loading race ui and register actions for timer and gpios
    """
    def __init__(self):
        super().__init__()
        self.ui = raceView.Ui_MainWindow()
        self.ui.setupUi(self)

        self.button_is_checked = False
        self.ui.actionButton.setCheckable(True)
        #self.ui.actionButton.released.connect(self.trigger_timer_action)
        self.ui.actionButton.released.connect(self.test)
        self.ui.actionButton.setChecked(self.button_is_checked)

        # Updater and Timer
        self.actual_time = None  # TODO: Move properties to own class?
        self.start_time = None
        self.measured_round_times = []
        self.rounds_to_drive = 3  # TODO: Set over input field

        self.updater = race_timer.Updater()
        self.updater.worker.update_progress.measured_time.connect(self.update_number)

        self.gpio = MotionSensor(constants.MOTION_SENSOR_PIN, queue_len=constants.MOTION_SENSOR_QUEUE_LENGTH)
        self.led = RGBLED(red=constants.LED_STRIP_RED_PIN, green=constants.LED_STRIP_GREEN_PIN, blue=constants.LED_STRIP_BLUE_PIN, initial_value=constants.LIGHT_RED)

    def test(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.NoIcon)
        msgBox.setText("<h1>Trest1</h1></br><hr></br>Test2")
        msgBox.setWindowTitle("Ergebnis")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()

    def trigger_timer_action(self):
        """
        Trigger the action for timer, make timer ready or abort proc
        """
        if self.button_is_checked:
            self.bal(constants.BUTTON_TEXT_GO, not self.button_is_checked, constants.LIGHT_RED, None)
            self.reset_race_time_tracking()
        else:
            self.bal(constants.BUTTON_TEXT_STOP, not self.button_is_checked, constants.LIGHT_GREEN, self.trigger_start_timer)

    def bal(self, button_text, button_checked, light_color, motion_action):
        """
        Switch button between ready and stop state
        :param button_text: Text to show in the button
        :param button_checked: Set if button is checked or unchecked
        :param light_color: Color for traffic light
        :param motion_action: Action to set for when_motion event
        """
        self.ui.actionButton.setText(button_text)
        self.button_is_checked = button_checked
        self.led.value = light_color
        self.gpio.when_motion = motion_action

    def reset_race_time_tracking(self):
        """
        Stop the time tracking proc and reset all values
        """
        self.stop_race_timer()
        self.set_time_values(None, None)
        self.ui.timeLabel.setText(constants.LABEL_TIMER_DEFAULT)

    def trigger_start_timer(self):
        """
        Trigger the action for timer, make timer ready or abort proc
        """
        self.led.value = constants.LIGHT_NO
        self.set_time_values(datetime.now(timezone.utc), 0)
        self.updater.start()
        self.gpio.when_motion = self.take_round_of_finish_race

    def take_round_of_finish_race(self):
        """
        Define the workflow to take round time or stop race.
        """
        if self.actual_time.total_seconds() < constants.TIMER_MINIMAL_RUNNING_TIME_SEC:
            print("Not yet")
            return

        race_finished = len(self.measured_round_times) == (self.rounds_to_drive - 1)
        if race_finished:
            self.stop_race_timer()

        accurate_mode = os.getenv("ACCURATE_MODE", "0")  # TODO: Set over input field
        if accurate_mode.isdigit() and int(accurate_mode) == 1:
            print('Use ACCURATE_MODE')
            self.update_stopwatch_time(datetime.now(timezone.utc))

        self.measured_round_times.append(self.actual_time)
        self.set_time_values(datetime.now(timezone.utc), None)
        self.ui.timeLabel.setText(constants.LABEL_TIMER_DEFAULT)

        if race_finished:
            self.bal(constants.BUTTON_TEXT_GO, False, constants.LIGHT_RED, None)

        print(str(self.measured_round_times))
        # TODO: Show final view with results and highlight best round

    def stop_race_timer(self):
        """
        Stop the updater and timer, wait until finish
        """
        self.updater.quit()
        self.updater.wait()

    def set_time_values(self, start_time, actual_time):
        """
        Set time values to desire values
        :param start_time: New value for class parameter start_time
        :param actual_time: New value for class parameter actual_time
        """
        self.start_time = start_time
        self.actual_time = actual_time

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
