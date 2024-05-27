import datetime

from PySide6.QtCore import QObject, Signal, QThread, QTimer


class WorkerSignal(QObject):
    latest_number = Signal(datetime.timedelta)


class Worker(QObject):
    def __init__(self):
        QObject.__init__(self)
        self.update_progress = WorkerSignal()
        self.start_time = None
        self.timer = QTimer()

    def update_label(self):
        print("update label started")
        try:
            measured_time = datetime.datetime.now(datetime.timezone.utc) - self.start_time
            self.update_progress.latest_number.emit(measured_time)
        except:
            print("Error, but just for testing...")
            self.update_progress.latest_number.emit("0")

    def main(self):
        print('Init worker')
        self.start_time = datetime.datetime.now(datetime.timezone.utc)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_label)
        self.thread().finished.connect(self.timer.stop)
        self.timer.start()


class Updater(QThread):
    def __init__(self):
        QThread.__init__(self)

        self.worker = Worker()

        # Move worker to another thread, to execute in parallel
        self.worker.moveToThread(self)

        # Set which method from Worker that should execute on the other thread.
        # In this case: Worker.main
        self.started.connect(self.worker.main)
