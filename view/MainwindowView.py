# pylint: skip-file

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QFont, QIcon)
from PySide6.QtWidgets import (QPushButton, QSizePolicy, QVBoxLayout, QWidget)


class UiMainWindow(object):
    def setup_ui(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"MainWindow")
        main_window.setWindowModality(Qt.WindowModal)
        main_window.resize(400, 600)
        size_policy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(main_window.sizePolicy().hasHeightForWidth())
        main_window.setSizePolicy(size_policy)
        icon = QIcon()
        icon.addFile(u"../../../../Bilder/coffee.jpg", QSize(), QIcon.Normal, QIcon.Off)
        main_window.setWindowIcon(icon)
        main_window.setToolButtonStyle(Qt.ToolButtonTextOnly)
        self.centralwidget = QWidget(main_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.button_start = QPushButton(self.centralwidget)
        self.button_start.setObjectName(u"button_start")
        size_policy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        size_policy1.setHorizontalStretch(0)
        size_policy1.setVerticalStretch(0)
        size_policy1.setHeightForWidth(self.button_start.sizePolicy().hasHeightForWidth())
        self.button_start.setSizePolicy(size_policy1)
        font = QFont()
        font.setPointSize(12)
        self.button_start.setFont(font)

        self.verticalLayout.addWidget(self.button_start)

        self.button_hitory = QPushButton(self.centralwidget)
        self.button_hitory.setObjectName(u"button_hitory")
        self.button_hitory.setEnabled(False)
        size_policy1.setHeightForWidth(self.button_hitory.sizePolicy().hasHeightForWidth())
        self.button_hitory.setSizePolicy(size_policy1)
        self.button_hitory.setFont(font)

        self.verticalLayout.addWidget(self.button_hitory)

        self.button_settings = QPushButton(self.centralwidget)
        self.button_settings.setObjectName(u"button_settings")
        size_policy1.setHeightForWidth(self.button_settings.sizePolicy().hasHeightForWidth())
        self.button_settings.setSizePolicy(size_policy1)
        self.button_settings.setFont(font)

        self.verticalLayout.addWidget(self.button_settings)

        main_window.setCentralWidget(self.centralwidget)

        self.retranslate_ui(main_window)

        QMetaObject.connectSlotsByName(main_window)

    # setupUi

    def retranslate_ui(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("MainWindow", u"RaceTracker", None))
        self.button_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.button_hitory.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.button_settings.setText(QCoreApplication.translate("MainWindow", u"Einstellungen", None))
    # retranslateUi
