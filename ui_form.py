# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QProgressBar,
    QPushButton, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Widget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setContextMenuPolicy(Qt.NoContextMenu)
        self.label.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.label)

        self.port_combo = QComboBox(self.groupBox)
        self.port_combo.setObjectName(u"port_combo")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.port_combo.sizePolicy().hasHeightForWidth())
        self.port_combo.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.port_combo)

        self.refresh_btn = QPushButton(self.groupBox)
        self.refresh_btn.setObjectName(u"refresh_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.refresh_btn.sizePolicy().hasHeightForWidth())
        self.refresh_btn.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.refresh_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.baud_combo = QComboBox(self.groupBox)
        self.baud_combo.addItem("")
        self.baud_combo.addItem("")
        self.baud_combo.addItem("")
        self.baud_combo.addItem("")
        self.baud_combo.addItem("")
        self.baud_combo.setObjectName(u"baud_combo")

        self.horizontalLayout_2.addWidget(self.baud_combo)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.connect_btn = QPushButton(self.groupBox)
        self.connect_btn.setObjectName(u"connect_btn")

        self.horizontalLayout_3.addWidget(self.connect_btn)

        self.disconnect_btn = QPushButton(self.groupBox)
        self.disconnect_btn.setObjectName(u"disconnect_btn")

        self.horizontalLayout_3.addWidget(self.disconnect_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.terminal_output = QTextEdit(self.groupBox_2)
        self.terminal_output.setObjectName(u"terminal_output")
        self.terminal_output.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.terminal_output)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.command_input = QLineEdit(self.groupBox_2)
        self.command_input.setObjectName(u"command_input")

        self.horizontalLayout_5.addWidget(self.command_input)

        self.send_command = QPushButton(self.groupBox_2)
        self.send_command.setObjectName(u"send_command")

        self.horizontalLayout_5.addWidget(self.send_command)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.verticalLayout_4.setStretch(1, 1)

        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(Widget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.script_input = QTextEdit(self.groupBox_3)
        self.script_input.setObjectName(u"script_input")

        self.verticalLayout_5.addWidget(self.script_input)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.load_file_btn = QPushButton(self.groupBox_3)
        self.load_file_btn.setObjectName(u"load_file_btn")

        self.horizontalLayout_6.addWidget(self.load_file_btn)

        self.save_file_btn = QPushButton(self.groupBox_3)
        self.save_file_btn.setObjectName(u"save_file_btn")

        self.horizontalLayout_6.addWidget(self.save_file_btn)

        self.start_script_btn = QPushButton(self.groupBox_3)
        self.start_script_btn.setObjectName(u"start_script_btn")

        self.horizontalLayout_6.addWidget(self.start_script_btn)

        self.stop_script_btn = QPushButton(self.groupBox_3)
        self.stop_script_btn.setObjectName(u"stop_script_btn")

        self.horizontalLayout_6.addWidget(self.stop_script_btn)

        self.clear_script_btn = QPushButton(self.groupBox_3)
        self.clear_script_btn.setObjectName(u"clear_script_btn")

        self.horizontalLayout_6.addWidget(self.clear_script_btn)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)

        self.horizontalLayout_7.addWidget(self.label_3)

        self.delay_combo = QComboBox(self.groupBox_3)
        self.delay_combo.addItem("")
        self.delay_combo.addItem("")
        self.delay_combo.addItem("")
        self.delay_combo.addItem("")
        self.delay_combo.addItem("")
        self.delay_combo.addItem("")
        self.delay_combo.addItem("")
        self.delay_combo.addItem("")
        self.delay_combo.setObjectName(u"delay_combo")

        self.horizontalLayout_7.addWidget(self.delay_combo)


        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        self.script_progress = QProgressBar(self.groupBox_3)
        self.script_progress.setObjectName(u"script_progress")
        self.script_progress.setValue(24)

        self.verticalLayout_5.addWidget(self.script_progress)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 5)
        self.verticalLayout.setStretch(2, 5)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"PySerial Terminal", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widget", u"Connection Settings", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Port:", None))
        self.refresh_btn.setText(QCoreApplication.translate("Widget", u"Referesh", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Baud Rate", None))
        self.baud_combo.setItemText(0, QCoreApplication.translate("Widget", u"9600", None))
        self.baud_combo.setItemText(1, QCoreApplication.translate("Widget", u"19200", None))
        self.baud_combo.setItemText(2, QCoreApplication.translate("Widget", u"38400", None))
        self.baud_combo.setItemText(3, QCoreApplication.translate("Widget", u"57600", None))
        self.baud_combo.setItemText(4, QCoreApplication.translate("Widget", u"115200", None))

        self.baud_combo.setCurrentText(QCoreApplication.translate("Widget", u"115200", None))
        self.connect_btn.setText(QCoreApplication.translate("Widget", u"Connect", None))
        self.disconnect_btn.setText(QCoreApplication.translate("Widget", u"DisConnect", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Widget", u"Terminal", None))
        self.send_command.setText(QCoreApplication.translate("Widget", u"Run", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Widget", u"Command Script", None))
        self.script_input.setPlaceholderText(QCoreApplication.translate("Widget", u"Enter multiple commands here, one per line or use the file buttons to load/save commands.", None))
        self.load_file_btn.setText(QCoreApplication.translate("Widget", u"Load From File", None))
        self.save_file_btn.setText(QCoreApplication.translate("Widget", u"Save To File", None))
        self.start_script_btn.setText(QCoreApplication.translate("Widget", u"Run Script", None))
        self.stop_script_btn.setText(QCoreApplication.translate("Widget", u"Stop Script", None))
        self.clear_script_btn.setText(QCoreApplication.translate("Widget", u"Clear Script", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Command Delay (ms)", None))
        self.delay_combo.setItemText(0, QCoreApplication.translate("Widget", u"10", None))
        self.delay_combo.setItemText(1, QCoreApplication.translate("Widget", u"20", None))
        self.delay_combo.setItemText(2, QCoreApplication.translate("Widget", u"30", None))
        self.delay_combo.setItemText(3, QCoreApplication.translate("Widget", u"50", None))
        self.delay_combo.setItemText(4, QCoreApplication.translate("Widget", u"100", None))
        self.delay_combo.setItemText(5, QCoreApplication.translate("Widget", u"200", None))
        self.delay_combo.setItemText(6, QCoreApplication.translate("Widget", u"500", None))
        self.delay_combo.setItemText(7, QCoreApplication.translate("Widget", u"1000", None))

    # retranslateUi

