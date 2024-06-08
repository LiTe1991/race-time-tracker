"""
    The timer which measure time and notify ui to calculate time and update label.
"""
from datetime import datetime, timezone

from PySide6.QtCore import QObject, Signal, QThread, QTimer


class WorkerSignal(QObject):
    """
        Needed signal to inform ui about actual time.
    """
    measured_time = Signal(datetime)


class Worker(QObject):
    """
        Contain the logic to start time and to measure time, also fire the event for ui update.
    """
    def __init__(self):
        QObject.__init__(self)
        self.update_progress = WorkerSignal()
        self.timer = QTimer()

    def post_time(self):
        """
            Emit the actual time to signal.
        """
        try:
            self.update_progress.measured_time.emit(datetime.now(timezone.utc))
        except:
            print("Error, but just for testing...")
            self.update_progress.measured_time.emit(datetime.min)

    def main(self):
        """
            Main function of worker to set timer and start this one.
        """
        print('Init worker')
        self.timer.setInterval(100)
        print('Connect timeout')
        self.timer.timeout.connect(self.post_time)
        print('Connect finished thread')
        self.thread().finished.connect(self.timer.stop)
        print('Start timer')
        try:
            print('Test: ' + str(self.thread().objectName()))
            self.timer.start()
        except:
            print("Error, but just for testing...")


class Updater(QThread):
    """
        Update which start the worker for time measure and move the thread.
    """
    def __init__(self):
        QThread.__init__(self)

        self.worker = Worker()

        # Move worker to another thread, to execute in parallel
        self.worker.moveToThread(self)

        # Set which method from Worker that should execute on the other thread.
        # In this case: Worker.main
        self.started.connect(self.worker.main)
