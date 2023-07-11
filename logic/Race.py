from PySide6.QtWidgets import QMainWindow
from view.RaceView import UiMainWindow


class RaceWindow(QMainWindow):
    def __init__(self):
        super(RaceWindow, self).__init__()
        self.ui = UiMainWindow()
        self.ui.setup_ui(self)
