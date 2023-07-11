# pylint: skip-file

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QAbstractSpinBox, QCheckBox, QFormLayout,
                               QGridLayout, QHBoxLayout, QLabel, QLayout,
                               QLineEdit, QListView, QPushButton, QSizePolicy,
                               QSpinBox, QVBoxLayout)


class UiSettings(object):
    def setup_ui(self, settings):
        if not settings.objectName():
            settings.setObjectName(u"Settings")
        settings.setWindowModality(Qt.WindowModal)
        settings.resize(1344, 756)
        size_policy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(settings.sizePolicy().hasHeightForWidth())
        settings.setSizePolicy(size_policy)
        self.gridLayout_2 = QGridLayout(settings)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_driver_settings = QLabel(settings)
        self.label_driver_settings.setObjectName(u"label_driver_settings")
        size_policy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        size_policy1.setHorizontalStretch(0)
        size_policy1.setVerticalStretch(0)
        size_policy1.setHeightForWidth(self.label_driver_settings.sizePolicy().hasHeightForWidth())
        self.label_driver_settings.setSizePolicy(size_policy1)
        font = QFont()
        font.setPointSize(20)
        self.label_driver_settings.setFont(font)
        self.label_driver_settings.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)

        self.gridLayout_2.addWidget(self.label_driver_settings, 1, 1, 1, 1)

        self.label_common_settings = QLabel(settings)
        self.label_common_settings.setObjectName(u"label_common_settings")
        size_policy1.setHeightForWidth(self.label_common_settings.sizePolicy().hasHeightForWidth())
        self.label_common_settings.setSizePolicy(size_policy1)
        self.label_common_settings.setFont(font)
        self.label_common_settings.setLayoutDirection(Qt.LeftToRight)
        self.label_common_settings.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)

        self.gridLayout_2.addWidget(self.label_common_settings, 1, 0, 1, 1)

        self.v_layout_common_settings = QVBoxLayout()
        self.v_layout_common_settings.setObjectName(u"v_layout_common_settings")
        self.v_layout_common_settings.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.formLayout.setFormAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.formLayout.setVerticalSpacing(6)
        self.label_pylonen_penaltytime = QLabel(settings)
        self.label_pylonen_penaltytime.setObjectName(u"label_pylonen_penaltytime")
        size_policy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        size_policy2.setHorizontalStretch(0)
        size_policy2.setVerticalStretch(0)
        size_policy2.setHeightForWidth(self.label_pylonen_penaltytime.sizePolicy().hasHeightForWidth())
        self.label_pylonen_penaltytime.setSizePolicy(size_policy2)
        self.label_pylonen_penaltytime.setMinimumSize(QSize(250, 0))
        font1 = QFont()
        font1.setPointSize(12)
        self.label_pylonen_penaltytime.setFont(font1)
        self.label_pylonen_penaltytime.setMargin(0)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_pylonen_penaltytime)

        self.spinBox_pylon_penaltytime = QSpinBox(settings)
        self.spinBox_pylon_penaltytime.setObjectName(u"spinBox_pylon_penaltytime")
        size_policy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        size_policy3.setHorizontalStretch(0)
        size_policy3.setVerticalStretch(0)
        size_policy3.setHeightForWidth(self.spinBox_pylon_penaltytime.sizePolicy().hasHeightForWidth())
        self.spinBox_pylon_penaltytime.setSizePolicy(size_policy3)
        self.spinBox_pylon_penaltytime.setMinimumSize(QSize(0, 0))
        self.spinBox_pylon_penaltytime.setLayoutDirection(Qt.LeftToRight)
        self.spinBox_pylon_penaltytime.setButtonSymbols(QAbstractSpinBox.PlusMinus)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.spinBox_pylon_penaltytime)

        self.v_layout_common_settings.addLayout(self.formLayout)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setVerticalSpacing(6)
        self.label_tor_penaltytime = QLabel(settings)
        self.label_tor_penaltytime.setObjectName(u"label_tor_penaltytime")
        size_policy3.setHeightForWidth(self.label_tor_penaltytime.sizePolicy().hasHeightForWidth())
        self.label_tor_penaltytime.setSizePolicy(size_policy3)
        self.label_tor_penaltytime.setMinimumSize(QSize(250, 0))
        self.label_tor_penaltytime.setFont(font1)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_tor_penaltytime)

        self.spinBox_tor_penaltytime = QSpinBox(settings)
        self.spinBox_tor_penaltytime.setObjectName(u"spinBox_tor_penaltytime")
        size_policy3.setHeightForWidth(self.spinBox_tor_penaltytime.sizePolicy().hasHeightForWidth())
        self.spinBox_tor_penaltytime.setSizePolicy(size_policy3)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.spinBox_tor_penaltytime)

        self.v_layout_common_settings.addLayout(self.formLayout_2)

        self.button_save_settings = QPushButton(settings)
        self.button_save_settings.setObjectName(u"button_save_settings")
        self.button_save_settings.setFont(font1)

        self.v_layout_common_settings.addWidget(self.button_save_settings)

        self.gridLayout_2.addLayout(self.v_layout_common_settings, 2, 0, 1, 1)

        self.v_layout_driver_settings = QVBoxLayout()
        self.v_layout_driver_settings.setObjectName(u"v_layout_driver_settings")
        self.list_basic_starter = QListView(settings)
        self.list_basic_starter.setObjectName(u"list_basic_starter")

        self.v_layout_driver_settings.addWidget(self.list_basic_starter)

        self.h_layout_name = QHBoxLayout()
        self.h_layout_name.setObjectName(u"h_layout_name")
        self.edit_firstname = QLineEdit(settings)
        self.edit_firstname.setObjectName(u"edit_firstname")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.edit_firstname.sizePolicy().hasHeightForWidth())
        self.edit_firstname.setSizePolicy(sizePolicy4)
        self.edit_firstname.setFont(font1)

        self.h_layout_name.addWidget(self.edit_firstname)

        self.edit_lastname = QLineEdit(settings)
        self.edit_lastname.setObjectName(u"edit_lastname")
        sizePolicy4.setHeightForWidth(self.edit_lastname.sizePolicy().hasHeightForWidth())
        self.edit_lastname.setSizePolicy(sizePolicy4)
        self.edit_lastname.setFont(font1)

        self.h_layout_name.addWidget(self.edit_lastname)

        self.check_guest = QCheckBox(settings)
        self.check_guest.setObjectName(u"check_guest")
        self.check_guest.setFont(font1)
        self.check_guest.setLayoutDirection(Qt.RightToLeft)

        self.h_layout_name.addWidget(self.check_guest)

        self.v_layout_driver_settings.addLayout(self.h_layout_name)

        self.button_add_driver = QPushButton(settings)
        self.button_add_driver.setObjectName(u"button_add_driver")
        self.button_add_driver.setFont(font1)

        self.v_layout_driver_settings.addWidget(self.button_add_driver)

        self.gridLayout_2.addLayout(self.v_layout_driver_settings, 2, 1, 1, 1)

        self.retranslate_ui(settings)

        QMetaObject.connectSlotsByName(settings)

    # setupUi

    def retranslate_ui(self, settings):
        settings.setWindowTitle(QCoreApplication.translate("Settings", u"Einstellungen", None))
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
