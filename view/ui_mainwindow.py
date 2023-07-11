# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"../../../../Bilder/coffee.jpg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(Qt.ToolButtonTextOnly)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.button_start = QPushButton(self.centralwidget)
        self.button_start.setObjectName(u"button_start")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.button_start.sizePolicy().hasHeightForWidth())
        self.button_start.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(12)
        self.button_start.setFont(font)

        self.verticalLayout.addWidget(self.button_start)

        self.button_hitory = QPushButton(self.centralwidget)
        self.button_hitory.setObjectName(u"button_hitory")
        self.button_hitory.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.button_hitory.sizePolicy().hasHeightForWidth())
        self.button_hitory.setSizePolicy(sizePolicy1)
        self.button_hitory.setFont(font)

        self.verticalLayout.addWidget(self.button_hitory)

        self.button_settings = QPushButton(self.centralwidget)
        self.button_settings.setObjectName(u"button_settings")
        sizePolicy1.setHeightForWidth(self.button_settings.sizePolicy().hasHeightForWidth())
        self.button_settings.setSizePolicy(sizePolicy1)
        self.button_settings.setFont(font)

        self.verticalLayout.addWidget(self.button_settings)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"RaceTracker", None))
        self.button_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.button_hitory.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.button_settings.setText(QCoreApplication.translate("MainWindow", u"Einstellungen", None))
    # retranslateUi

