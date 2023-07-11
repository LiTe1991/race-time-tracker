from PySide6.QtWidgets import QMainWindow
from view.ui_test import Ui_MainWindow


class RaceWindow(QMainWindow):
    def __init__(self):
        super(RaceWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
