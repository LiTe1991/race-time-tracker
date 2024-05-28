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
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

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
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.timeLabel = QLabel(self.centralwidget)
        self.timeLabel.setObjectName(u"timeLabel")
        font = QFont()
        font.setFamilies([u"Bahnschrift SemiLight"])
        font.setPointSize(180)
        font.setBold(True)
        self.timeLabel.setFont(font)
        self.timeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.timeLabel, 0, 1, 1, 2)

        self.actionButton = QPushButton(self.centralwidget)
        self.actionButton.setObjectName(u"actionButton")
        font1 = QFont()
        font1.setPointSize(20)
        self.actionButton.setFont(font1)

        self.gridLayout.addWidget(self.actionButton, 1, 1, 1, 2)

        self.test = QPushButton(self.centralwidget)
        self.test.setObjectName(u"test")
        self.test.setEnabled(False)
        sizePolicy.setHeightForWidth(self.test.sizePolicy().hasHeightForWidth())
        self.test.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(20)
        font2.setKerning(False)
        self.test.setFont(font2)
        self.test.setAutoFillBackground(False)
        self.test.setStyleSheet(u"background-color: rgba(255, 0, 0, 1);\n"
"border: none;")

        self.gridLayout.addWidget(self.test, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Time Tracker", None))
        self.timeLabel.setText(QCoreApplication.translate("MainWindow", u"0:00:00.000000", None))
        self.actionButton.setText(QCoreApplication.translate("MainWindow", u"Ready", None))
        self.test.setText("")
    # retranslateUi

