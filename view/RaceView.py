# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QFont, QIcon)
from PySide6.QtWidgets import (QGridLayout, QLabel, QListView, QPushButton, QSizePolicy, QWidget)


class UiMainWindow(object):
    def setup_ui(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"MainWindow")
        main_window.resize(1920, 1080)
        size_policy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(main_window.sizePolicy().hasHeightForWidth())
        main_window.setSizePolicy(size_policy)
        icon = QIcon()
        icon.addFile(u"../../Bilder/Backgrounds/1080p_m4_liberty_2.jpg", QSize(), QIcon.Normal, QIcon.Off)
        main_window.setWindowIcon(icon)
        main_window.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.centralwidget = QWidget(main_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.testTime = QLabel(self.centralwidget)
        self.testTime.setObjectName(u"testTime")
        font = QFont()
        font.setPointSize(120)
        font.setBold(True)
        self.testTime.setFont(font)
        self.testTime.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.testTime, 0, 0, 1, 2)

        self.start = QPushButton(self.centralwidget)
        self.start.setObjectName(u"start")

        self.gridLayout.addWidget(self.start, 1, 0, 1, 1)

        self.stop = QPushButton(self.centralwidget)
        self.stop.setObjectName(u"stop")

        self.gridLayout.addWidget(self.stop, 1, 1, 1, 1)

        self.listView = QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")
        size_policy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        size_policy1.setHorizontalStretch(0)
        size_policy1.setVerticalStretch(0)
        size_policy1.setHeightForWidth(self.listView.sizePolicy().hasHeightForWidth())
        self.listView.setSizePolicy(size_policy1)

        self.gridLayout.addWidget(self.listView, 0, 2, 1, 1)

        main_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(main_window)

        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslate_ui(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("MainWindow", u"Time Tracker", None))
        self.testTime.setText(QCoreApplication.translate("MainWindow", u"00:00:00.000", None))
        self.start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.stop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
    # retranslateUi

