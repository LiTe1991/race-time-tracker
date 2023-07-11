import sys

from PySide6.QtCore import QThreadPool, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QProgressDialog, QPushButton

from logic.dataaccess.DBSetupWorker import DBSetupWorker
from view.ui_mainwindow import Ui_MainWindow
from logic.Settings import SettingsWindow
from logic.Race import RaceWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.threadpool = QThreadPool()
        self.threadpool.setMaxThreadCount(1)

        self.proc = QProgressDialog("Datenbank wird initialisiert.", "Abbrechen", 0, 0, self)
        close_button = QPushButton('Abbrechen')
        close_button.setEnabled(False)
        self.proc.setWindowTitle(None)
        self.proc.setWindowModality(Qt.WindowModal)
        self.proc.setCancelButton(close_button)
        self.proc.show()

        db_worker = DBSetupWorker(self)
        db_worker.signals.progress.connect(self.db_init_process)
        db_worker.signals.finished.connect(self.db_init_done)
        self.threadpool.start(db_worker)

        self.window = None
        self.ui.button_start.clicked.connect(self.open_race_window)
        self.ui.button_settings.clicked.connect(self.open_settings_window)

    def db_init_process(self, act, maxi):
        print("Step " + str(act) + " of " + str(maxi) + " done")
        self.proc.setMaximum(maxi)
        self.proc.setValue(act)

    def db_init_done(self, message):
        print(str(message))
        self.proc.close()

    def open_settings_window(self):
        if self.window is None:
            self.window = SettingsWindow()
            self.window.show()
        else:
            self.window.close()
            self.window = None

    def open_race_window(self):
        if self.window is None:
            self.window = RaceWindow()
            self.window.show()
        else:
            self.window.close()
            self.window = None


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
