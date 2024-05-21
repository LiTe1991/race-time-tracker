"""
    The bla
"""
import time
from datetime import datetime, timedelta

from PySide6.QtCore import QTimer, Signal, QRunnable, QObject
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import Button

class StopwatchSignal(QObject):
    testSig = Signal(timedelta)

class Stopwatch(QRunnable):
    """
        Bla
    """
    def __init__(self):
        super().__init__()

        self.signal = StopwatchSignal()

        self.start_time = None

        # self.factory = None
        # self.gpio = None

    def take_actual_measured_time(self):
        """
            Take the actual time and subtract the start time
        """
        ela = datetime.now() - self.start_time
        self.signal.testSig.emit(ela)

    def execute_stopwatch(self):
        """
            Test
        """
        self.start_time = datetime.now()

        timer = QTimer()
        timer.timeout.connect(self.take_actual_measured_time)
        timer.start(50)
        ##self.factory = PiGPIOFactory(host='192.168.178.44')
        # self.gpio = Button(4, pin_factory=self.factory)

        # self.gpio.when_released = self.trigger_timer_action

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

    def run(self):
        self.execute_stopwatch()
        i = 0
        while i < 100:
            print('test')
            time.sleep(1)
            i+=1
