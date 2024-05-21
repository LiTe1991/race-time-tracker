"""
    The main application which is used during start proc etc.
"""
import datetime
import sys

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QMainWindow
from gpiozero import Button, MotionSensor, LineSensor
from gpiozero.pins.pigpio import PiGPIOFactory

import view.RaceView as raceView


class MainWindow(QMainWindow):
    """
        Main Window contain logic for loading race ui and register actions for timer and gpios
    """
    def __init__(self):
        super().__init__()
        self.ui = raceView.Ui_MainWindow()
        self.ui.setupUi(self)

        self.start_time = None

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_stopwatch_time)

        self.button_is_checked = True
        self.ui.actionButton.setCheckable(True)
        self.ui.actionButton.released.connect(self.trigger_timer_action)
        self.ui.actionButton.setChecked(self.button_is_checked)

        self.factory = PiGPIOFactory(host='192.168.178.44')
        self.gpio = MotionSensor(22, pin_factory=self.factory)

        self.gpio.when_motion = self.trigger_timer_action

        # elapsed_time = datetime.datetime.now() - measured_time
        # def trigger_timer_action(self):
        #    """
        #        Trigger the action for timer, make timer ready or abort proc
        #    """
        #    print(self.gpio.is_pressed)
        #    if self.start_time is None:
        #        self.ui.actionButton.setText("Abbrechen")
        #        self.timer.start()
        #        self.start_time = datetime.datetime.now()
        #    else:
        #        self.ui.actionButton.setText("Ready")
        #        self.timer.stop()
        #        self.start_time = None

    def trigger_timer_action(self):
        """
            Trigger the action for timer, make timer ready or abort proc
        """
        #print('start_timer')
        print('GPIO:' + str(self.gpio.is_active))
        print('GPIO3:' + str(self.gpio.active_time))

        #if self.button_is_checked:
        #    self.stop_timer()
        #else:
        #    self.start_time = datetime.datetime.now()
        #    self.timer.start(50)
        #    self.ui.actionButton.setText("Stop")

    def stop_timer(self):
        """
            Test
        """
        print('stop_timer')
        self.timer.stop()
        self.update_stopwatch_time()
        self.ui.actionButton.setText("Ready")

    def update_stopwatch_time(self):
        """
            Update the timer label and set actual measured time
        """
        print('update_Test')
        measured_time = datetime.datetime.now() - self.start_time
        print(str(datetime.datetime.now()) + " " + str(self.start_time))
        print('Update:' + str(measured_time))
        self.ui.timeLabel.setText(str(measured_time))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
