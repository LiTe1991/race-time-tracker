# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QFormLayout,
    QGridLayout, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QListView, QPushButton, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.resize(1344, 756)
        self.gridLayout_2 = QGridLayout(Settings)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_driver_settings = QLabel(Settings)
        self.label_driver_settings.setObjectName(u"label_driver_settings")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_driver_settings.sizePolicy().hasHeightForWidth())
        self.label_driver_settings.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(20)
        self.label_driver_settings.setFont(font)
        self.label_driver_settings.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout_2.addWidget(self.label_driver_settings, 1, 1, 1, 1)

        self.label_common_settings = QLabel(Settings)
        self.label_common_settings.setObjectName(u"label_common_settings")
        sizePolicy.setHeightForWidth(self.label_common_settings.sizePolicy().hasHeightForWidth())
        self.label_common_settings.setSizePolicy(sizePolicy)
        self.label_common_settings.setFont(font)
        self.label_common_settings.setLayoutDirection(Qt.LeftToRight)
        self.label_common_settings.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout_2.addWidget(self.label_common_settings, 1, 0, 1, 1)

        self.v_layout_common_settings = QVBoxLayout()
        self.v_layout_common_settings.setObjectName(u"v_layout_common_settings")
        self.v_layout_common_settings.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.formLayout.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.formLayout.setVerticalSpacing(6)
        self.label_pylonen_penaltytime = QLabel(Settings)
        self.label_pylonen_penaltytime.setObjectName(u"label_pylonen_penaltytime")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_pylonen_penaltytime.sizePolicy().hasHeightForWidth())
        self.label_pylonen_penaltytime.setSizePolicy(sizePolicy1)
        self.label_pylonen_penaltytime.setMinimumSize(QSize(250, 0))
        font1 = QFont()
        font1.setPointSize(12)
        self.label_pylonen_penaltytime.setFont(font1)
        self.label_pylonen_penaltytime.setMargin(0)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_pylonen_penaltytime)

        self.spinBox_pylon_penaltytime = QSpinBox(Settings)
        self.spinBox_pylon_penaltytime.setObjectName(u"spinBox_pylon_penaltytime")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.spinBox_pylon_penaltytime.sizePolicy().hasHeightForWidth())
        self.spinBox_pylon_penaltytime.setSizePolicy(sizePolicy2)
        self.spinBox_pylon_penaltytime.setMinimumSize(QSize(0, 0))
        self.spinBox_pylon_penaltytime.setLayoutDirection(Qt.LeftToRight)
        self.spinBox_pylon_penaltytime.setButtonSymbols(QAbstractSpinBox.PlusMinus)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.spinBox_pylon_penaltytime)


        self.v_layout_common_settings.addLayout(self.formLayout)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setVerticalSpacing(6)
        self.label_tor_penaltytime = QLabel(Settings)
        self.label_tor_penaltytime.setObjectName(u"label_tor_penaltytime")
        sizePolicy2.setHeightForWidth(self.label_tor_penaltytime.sizePolicy().hasHeightForWidth())
        self.label_tor_penaltytime.setSizePolicy(sizePolicy2)
        self.label_tor_penaltytime.setMinimumSize(QSize(250, 0))
        self.label_tor_penaltytime.setFont(font1)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_tor_penaltytime)

        self.spinBox_tor_penaltytime = QSpinBox(Settings)
        self.spinBox_tor_penaltytime.setObjectName(u"spinBox_tor_penaltytime")
        sizePolicy2.setHeightForWidth(self.spinBox_tor_penaltytime.sizePolicy().hasHeightForWidth())
        self.spinBox_tor_penaltytime.setSizePolicy(sizePolicy2)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.spinBox_tor_penaltytime)


        self.v_layout_common_settings.addLayout(self.formLayout_2)

        self.button_save_settings = QPushButton(Settings)
        self.button_save_settings.setObjectName(u"button_save_settings")
        self.button_save_settings.setFont(font1)

        self.v_layout_common_settings.addWidget(self.button_save_settings)


        self.gridLayout_2.addLayout(self.v_layout_common_settings, 2, 0, 1, 1)

        self.v_layout_driver_settings = QVBoxLayout()
        self.v_layout_driver_settings.setObjectName(u"v_layout_driver_settings")
        self.list_basic_starter = QListView(Settings)
        self.list_basic_starter.setObjectName(u"list_basic_starter")

        self.v_layout_driver_settings.addWidget(self.list_basic_starter)

        self.h_layout_name = QHBoxLayout()
        self.h_layout_name.setObjectName(u"h_layout_name")
        self.edit_firstname = QLineEdit(Settings)
        self.edit_firstname.setObjectName(u"edit_firstname")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.edit_firstname.sizePolicy().hasHeightForWidth())
        self.edit_firstname.setSizePolicy(sizePolicy3)
        self.edit_firstname.setFont(font1)

        self.h_layout_name.addWidget(self.edit_firstname)

        self.edit_lastname = QLineEdit(Settings)
        self.edit_lastname.setObjectName(u"edit_lastname")
        sizePolicy3.setHeightForWidth(self.edit_lastname.sizePolicy().hasHeightForWidth())
        self.edit_lastname.setSizePolicy(sizePolicy3)
        self.edit_lastname.setFont(font1)

        self.h_layout_name.addWidget(self.edit_lastname)

        self.check_guest = QCheckBox(Settings)
        self.check_guest.setObjectName(u"check_guest")
        self.check_guest.setFont(font1)
        self.check_guest.setLayoutDirection(Qt.RightToLeft)

        self.h_layout_name.addWidget(self.check_guest)


        self.v_layout_driver_settings.addLayout(self.h_layout_name)

        self.button_add_driver = QPushButton(Settings)
        self.button_add_driver.setObjectName(u"button_add_driver")

        self.v_layout_driver_settings.addWidget(self.button_add_driver)


        self.gridLayout_2.addLayout(self.v_layout_driver_settings, 2, 1, 1, 1)


        self.retranslateUi(Settings)

        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"Einstellungen", None))
        self.label_driver_settings.setText(QCoreApplication.translate("Settings", u"Fahrer Einstellungen:", None))
        self.label_common_settings.setText(QCoreApplication.translate("Settings", u"Allgemeine Einstellungen:", None))
        self.label_pylonen_penaltytime.setText(QCoreApplication.translate("Settings", u"Strafsekunden Pylone", None))
        self.spinBox_pylon_penaltytime.setSuffix(QCoreApplication.translate("Settings", u" Sekunden", None))
        self.label_tor_penaltytime.setText(QCoreApplication.translate("Settings", u"Strafsekunden Tor", None))
        self.spinBox_tor_penaltytime.setSuffix(QCoreApplication.translate("Settings", u" Sekunden", None))
        self.button_save_settings.setText(QCoreApplication.translate("Settings", u"Einstellungen speichern", None))
        self.edit_firstname.setPlaceholderText(QCoreApplication.translate("Settings", u"Vorname", None))
        self.edit_lastname.setPlaceholderText(QCoreApplication.translate("Settings", u"Nachname", None))
        self.check_guest.setText(QCoreApplication.translate("Settings", u"Gast", None))
        self.button_add_driver.setText(QCoreApplication.translate("Settings", u"Fahrer hinzuf\u00fcgen", None))
    # retranslateUi

