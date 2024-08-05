# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RaceView.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QListView,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1080)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"../../Bilder/Backgrounds/1080p_m4_liberty_2.jpg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.action_set_rounds = QAction(MainWindow)
        self.action_set_rounds.setObjectName(u"action_set_rounds")
        self.action_set_sensitivity = QAction(MainWindow)
        self.action_set_sensitivity.setObjectName(u"action_set_sensitivity")
        self.action_set_min_round_time = QAction(MainWindow)
        self.action_set_min_round_time.setObjectName(u"action_set_min_round_time")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.actionButton = QPushButton(self.centralwidget)
        self.actionButton.setObjectName(u"actionButton")
        font = QFont()
        font.setPointSize(20)
        self.actionButton.setFont(font)

        self.gridLayout.addWidget(self.actionButton, 1, 2, 1, 2)

        self.roundLabel = QLabel(self.centralwidget)
        self.roundLabel.setObjectName(u"roundLabel")
        sizePolicy.setHeightForWidth(self.roundLabel.sizePolicy().hasHeightForWidth())
        self.roundLabel.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift SemiLight"])
        font1.setPointSize(16)
        self.roundLabel.setFont(font1)
        self.roundLabel.setTextFormat(Qt.TextFormat.AutoText)
        self.roundLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.roundLabel.setWordWrap(False)

        self.gridLayout.addWidget(self.roundLabel, 1, 1, 1, 1)

        self.timeLabel = QLabel(self.centralwidget)
        self.timeLabel.setObjectName(u"timeLabel")
        font2 = QFont()
        font2.setFamilies([u"Bahnschrift SemiLight"])
        font2.setPointSize(180)
        font2.setBold(True)
        self.timeLabel.setFont(font2)
        self.timeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.timeLabel, 0, 2, 1, 2)

        self.test = QPushButton(self.centralwidget)
        self.test.setObjectName(u"test")
        self.test.setEnabled(False)
        sizePolicy.setHeightForWidth(self.test.sizePolicy().hasHeightForWidth())
        self.test.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setPointSize(20)
        font3.setKerning(False)
        self.test.setFont(font3)
        self.test.setAutoFillBackground(False)
        self.test.setStyleSheet(u"background-color: rgba(255, 0, 0, 1);\n"
"border: none;")

        self.gridLayout.addWidget(self.test, 1, 0, 1, 1)

        self.listView = QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.listView.sizePolicy().hasHeightForWidth())
        self.listView.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.listView, 2, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1920, 33))
        self.menuEinstellungen = QMenu(self.menuBar)
        self.menuEinstellungen.setObjectName(u"menuEinstellungen")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuEinstellungen.menuAction())
        self.menuEinstellungen.addAction(self.action_set_rounds)
        self.menuEinstellungen.addAction(self.action_set_sensitivity)
        self.menuEinstellungen.addAction(self.action_set_min_round_time)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Time Tracker", None))
        self.action_set_rounds.setText(QCoreApplication.translate("MainWindow", u"Runden konfigurieren", None))
        self.action_set_sensitivity.setText(QCoreApplication.translate("MainWindow", u"Empfindlichkeit konfigurieren", None))
        self.action_set_min_round_time.setText(QCoreApplication.translate("MainWindow", u"Min. Rundenzeit konfigurieren", None))
        self.actionButton.setText(QCoreApplication.translate("MainWindow", u"Ready", None))
        self.roundLabel.setText(QCoreApplication.translate("MainWindow", u"Runde: {str}/{end}", None))
        self.timeLabel.setText(QCoreApplication.translate("MainWindow", u"0:00:00.000000", None))
        self.test.setText("")
        self.menuEinstellungen.setTitle(QCoreApplication.translate("MainWindow", u"Einstellungen", None))
    # retranslateUi

