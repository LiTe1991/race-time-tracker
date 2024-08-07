"""
    The main application which is used during start proc etc.
"""
import sys

from datetime import datetime, timezone

from PySide6.QtCore import Slot
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QApplication, QMainWindow, QInputDialog

from gpiozero import MotionSensor, RGBLED

from view import RaceView as raceView
from logic import race_timer, race
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
        self.ui.actionButton.released.connect(self.trigger_timer_action)
        self.ui.actionButton.setChecked(self.button_is_checked)

        self.race = race.Race()

        # Updater and Timer
        self.updater = race_timer.Updater()
        self.updater.worker.update_progress.measured_time.connect(self.update_time)

        self.ui.action_set_rounds.triggered.connect(self.show_rounds_input_dialog)
        self.ui.action_set_sensitivity.triggered.connect(self.show_sensitivity_input_dialog)
        self.ui.action_set_min_round_time.triggered.connect(self.show_min_round_time_input_dialog)

        self.model = QStandardItemModel()
        self.ui.roundList.setModel(self.model)

        self.set_rounds_in_label()

        self.gpio = MotionSensor(constants.MOTION_SENSOR_PIN, queue_len=constants.MOTION_SENSOR_QUEUE_LENGTH)
        self.led = RGBLED(red=constants.LED_STRIP_RED_PIN, green=constants.LED_STRIP_GREEN_PIN,
                          blue=constants.LED_STRIP_BLUE_PIN, initial_value=constants.LIGHT_RED)

    def trigger_timer_action(self):
        """
        Trigger the action for timer, make timer ready or abort proc
        """
        self.reset_race_time_tracking()

        if self.button_is_checked:
            self.switch_button_action(constants.BUTTON_TEXT_GO, not self.button_is_checked, constants.LIGHT_RED, None)
        else:
            self.switch_button_action(constants.BUTTON_TEXT_STOP, not self.button_is_checked, constants.LIGHT_GREEN, self.trigger_start_timer)

    def switch_button_action(self, button_text, button_checked, light_color, motion_action):
        """
        Switch button between ready and stop state.
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
        self.race.reset_race()
        self.set_rounds_in_label()
        self.model.clear()
        self.ui.timeLabel.setText(constants.LABEL_TIMER_DEFAULT)

    def trigger_start_timer(self):
        """
        Trigger the action for timer, make timer ready or abort proc
        """
        self.led.value = constants.LIGHT_NO
        self.race.set_time_values(datetime.now(timezone.utc), 0)
        self.race.actual_round = 1
        self.set_rounds_in_label()
        self.updater.start()
        self.gpio.when_motion = self.take_round_or_finish_race

    def take_round_or_finish_race(self):
        """
        Define the workflow to take round time or stop race.
        """
        if not self.race.min_round_time_reached():
            print("Not yet")
            return

        if self.race.is_race_finished():
            print("Race finished")
            self.stop_race_timer()
            self.race.append_round_to_race()
            self.add_round_time_to_list()
            self.switch_button_action(constants.BUTTON_TEXT_GO, False, constants.LIGHT_RED, None)
            print(str(self.race.measured_round_times))
            return

        self.race.append_round_to_race()
        self.set_rounds_in_label()
        self.add_round_time_to_list()

    def stop_race_timer(self):
        """
        Stop the updater and timer, wait until finish
        """
        self.updater.quit()
        self.updater.wait()

    def set_rounds_in_label(self):
        """
        Update the rounds label and set the max rounds and actual_round
        """
        self.ui.roundLabel.setText(constants.LABEL_ROUND_COUNTER.replace("{str}", str(self.race.actual_round)).replace("{end}", str(self.race.rounds_to_drive)))

    def add_round_time_to_list(self):
        """
        Add last round time to list view
        """
        self.model.appendRow(QStandardItem(constants.LABEL_ROUND_TIME.replace("{rnd}", str(self.race.actual_round - 1)).replace("{time}", str(self.race.measured_round_times[len(self.race.measured_round_times) - 1]))))

    def update_stopwatch_time(self, time: datetime):
        """
            Test
        :param time:
        """
        self.race.update_actual_time(time)
        self.ui.timeLabel.setText(str(self.race.actual_time))

    @Slot(datetime)
    def update_time(self, val):
        """
        Slot which receive the signal from timer worker.
        :param val: The measured time.
        """
        self.update_stopwatch_time(val)

    def show_rounds_input_dialog(self):
        """
        Show an input dialog to set the rounds to drive
        """
        test = QInputDialog()
        test.setWindowTitle("Runden konfigurieren")
        test.setLabelText("Bitte Rundenanzahl eingeben:")
        test.setInputMode(QInputDialog.InputMode.IntInput)
        test.setIntMinimum(1)
        test.setIntMaximum(10)
        test.setIntValue(self.race.rounds_to_drive)
        test.intValueSelected.connect(self.update_rounds_to_drive)
        test.exec()

    def show_sensitivity_input_dialog(self):
        """
        Show an input dialog to set the sensitivity of motion sensor
        """
        test = QInputDialog()
        test.setWindowTitle("Empfindlichkeit konfigurieren")
        test.setLabelText("Bitte Empfindlichkeit eingeben:")
        test.setInputMode(QInputDialog.InputMode.IntInput)
        test.setIntMinimum(1)
        test.setIntMaximum(20)
        test.setIntValue(constants.MOTION_SENSOR_QUEUE_LENGTH)
        test.intValueSelected.connect(self.update_sensitivity_queue_length)
        test.exec()

    def show_min_round_time_input_dialog(self):
        """
        Show an input dialog to set the sensitivity of motion sensor
        """
        test = QInputDialog()
        test.setWindowTitle("Min. Rundenzeit konfigurieren")
        test.setLabelText("Bitte minimale Rundenzeit eingeben:")
        test.setInputMode(QInputDialog.InputMode.IntInput)
        test.setIntMinimum(1)
        test.setIntMaximum(30)
        test.setIntValue(self.race.min_round_time)
        test.intValueSelected.connect(self.update_min_round_time)
        test.exec()

    def update_rounds_to_drive(self, val1):
        """
        Signal action to update rounds from settings
        :param val1: Number of rounds
        """
        self.race.rounds_to_drive = val1
        self.set_rounds_in_label()

    def update_sensitivity_queue_length(self, val1):
        """
        Signal action to update sensitivity over queue length from settings
        :param val1: Number of queue length
        """
        self.gpio.close()
        self.gpio = MotionSensor(constants.MOTION_SENSOR_PIN, queue_len=val1)

    def update_min_round_time(self, val1):
        """
        Signal action to update min time per rounds from settings
        :param val1: Number of rounds
        """
        self.race.min_round_time = val1


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
