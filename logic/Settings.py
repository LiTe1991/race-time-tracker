from PySide6.QtWidgets import QWidget
from view.SettingsView import UiSettings


class SettingsWindow(QWidget):
    def __init__(self):
        super(SettingsWindow, self).__init__()
        self.ui = UiSettings()
        self.ui.setup_ui(self)
