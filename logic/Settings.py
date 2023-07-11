from PySide6.QtWidgets import QWidget
from view.ui_settings import Ui_Settings


class SettingsWindow(QWidget):
    def __init__(self):
        super(SettingsWindow, self).__init__()
        self.ui = Ui_Settings()
        self.ui.setupUi(self)
        