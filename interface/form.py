# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'objectWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class FrontWindow(object):
    def setup_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setStyleSheet("background-color: #3C3C3B;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.buttonEncrypt = QtWidgets.QPushButton(self.centralwidget)
        self.buttonEncrypt.setGeometry(QtCore.QRect(10, 280, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.buttonEncrypt.setFont(font)
        self.buttonEncrypt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonEncrypt.setStyleSheet("QPushButton {\n"
                                         "  background-color: #1F1F20;\n"
                                         "  border-style: solid;\n"
                                         "  border: 1px solid #1e1e1e;\n"
                                         "  border-radius: 5;\n"
                                         "  padding: 1px 0px 1px 0px;\n"
                                         "  color:#00ee00;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:pressed {\n"
                                         "    background-color: #181819\n"
                                         "}\n"
                                         "\n"
                                         " QPushButton:hover\n"
                                         "{\n"
                                         "    border: 2px solid #00ee00;\n"
                                         "    color: #00ee00;\n"
                                         "}")
        self.buttonEncrypt.setObjectName("buttonEncrypt")
        self.buttonDecrypt = QtWidgets.QPushButton(self.centralwidget)
        self.buttonDecrypt.setGeometry(QtCore.QRect(170, 280, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.buttonDecrypt.setFont(font)
        self.buttonDecrypt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonDecrypt.setStyleSheet("QPushButton {\n"
                                         "  background-color: #1F1F20;\n"
                                         "  border-style: solid;\n"
                                         "  border: 1px solid #1e1e1e;\n"
                                         "  border-radius: 5;\n"
                                         "  padding: 1px 0px 1px 0px;\n"
                                         "  color:#00ee00;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:pressed {\n"
                                         "    background-color: #181819;\n"
                                         "}\n"
                                         "\n"
                                         " QPushButton:hover\n"
                                         "{\n"
                                         "    border: 2px solid #00ee00;\n"
                                         "    color: #00ee00;\n"
                                         "}")
        self.buttonDecrypt.setObjectName("buttonDecrypt")
        self.keyLine = QtWidgets.QLineEdit(self.centralwidget)
        self.keyLine.setGeometry(QtCore.QRect(320, 280, 251, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 34, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 34, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 34, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 34, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 34, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 34, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 34, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 34, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 34, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 34, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 34, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 34, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.keyLine.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.keyLine.setFont(font)
        self.keyLine.setStyleSheet("QLineEdit {\n"
                                   "  background-color: #1F1F20;\n"
                                   "  border-style: solid;\n"
                                   "  border: 1px solid #1e1e1e;\n"
                                   "  border-radius: 5;\n"
                                   "  padding: 1px 0px 1px 0px;\n"
                                   "  color: #FF2200;\n"
                                   "}\n"
                                   "\n"
                                   " QLineEdit:hover\n"
                                   "{\n"
                                   "    border: 2px solid red;\n"
                                   "    color: red;\n"
                                   "}\n"
                                   "\n"
                                   "QLineEdit[echoMode=\"2\"] {\n"
                                   "    lineedit-password-character: 9679;\n"
                                   "}\n"
                                   "")
        self.keyLine.setObjectName("keyLine")
        self.resultText = QtWidgets.QTextEdit(self.centralwidget)
        self.resultText.setGeometry(QtCore.QRect(10, 320, 781, 251))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 238, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 238, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 238, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 238, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 238, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 238, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 238, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 238, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 238, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 238, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 238, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 238, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.resultText.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.resultText.setFont(font)
        self.resultText.setStyleSheet("QTextEdit {\n"
                                      "  background-color: #1F1F20;\n"
                                      "  border-style: solid;\n"
                                      "  border: 1px solid #1e1e1e;\n"
                                      "  border-radius: 5;\n"
                                      "  padding: 1px 0px 1px 0px;\n"
                                      "  color: #00ee00;\n"
                                      "}\n"
                                      "\n"
                                      "")
        self.resultText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.resultText.setObjectName("resultText")
        self.testForAction = QtWidgets.QTextEdit(self.centralwidget)
        self.testForAction.setGeometry(QtCore.QRect(10, 10, 781, 261))
        self.testForAction.setMinimumSize(QtCore.QSize(1, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 238, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 238, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 238, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 238, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 238, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 238, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 238, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 238, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 238, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 238, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 238, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 238, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.testForAction.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.testForAction.setFont(font)
        self.testForAction.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.testForAction.setStyleSheet("QTextEdit {\n"
                                         " background-color: #1F1F20;\n"
                                         "  border-style: solid;\n"
                                         "  border: 1px solid #1e1e1e;\n"
                                         "  border-radius: 5;\n"
                                         "  padding: 1px 0px 1px 0px;\n"
                                         "  color: #00ee00;\n"
                                         "}\n"
                                         "\n"
                                         "")
        self.testForAction.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.testForAction.setObjectName("testForAction")
        self.choiceBox = QtWidgets.QComboBox(self.centralwidget)
        self.choiceBox.setGeometry(QtCore.QRect(580, 280, 211, 31))
        self.choiceBox.setStyleSheet("QComboBox\n"
                                     "{\n"
                                     "    subcontrol-origin: padding;\n"
                                     "    subcontrol-position: top right;\n"
                                     "    selection-background-color: #111;\n"
                                     "    selection-color: #00ee00;\n"
                                     "    color: #00ee00;\n"
                                     "    background-color: #1E1E1E;\n"
                                     "    border-style: solid;\n"
                                     "    border: 1px solid #1e1e1e;\n"
                                     "    border-radius: 5;\n"
                                     "    padding: 1px 0px 1px 10px;\n"
                                     "}\n"
                                     "\n"
                                     "\n"
                                     "QComboBox:hover, QPushButton:hover\n"
                                     "{\n"
                                     "    border: 2px solid#00ee00;\n"
                                     "    color: #00ee00;\n"
                                     "}\n"
                                     "\n"
                                     "QComboBox:on\n"
                                     "{\n"
                                     "    padding-top: 0px;\n"
                                     "    padding-left: 0px;\n"
                                     "    color:#00ee00;\n"
                                     "    background-color: #181819;\n"
                                     "    selection-background-color: #ffaa00;\n"
                                     "    padding: 1px 0px 1px 10px;\n"
                                     "}\n"
                                     "\n"
                                     "QComboBox:!on\n"
                                     "{\n"
                                     "    color:#00ee00;\n"
                                     "    background-color: #1E1E1E;\n"
                                     "}\n"
                                     "\n"
                                     "QComboBox QAbstractItemView\n"
                                     "{\n"
                                     "    border: 2px solid darkgray;\n"
                                     "    color: #181819;\n"
                                     "    selection-background-color: #181819;\n"
                                     "}\n"
                                     "\n"
                                     "QComboBox::drop-down\n"
                                     "{\n"
                                     "     subcontrol-origin: padding;\n"
                                     "     subcontrol-position: top right;\n"
                                     "     width: 15px;\n"
                                     "     color: green;\n"
                                     "     border-left-width: 0px;\n"
                                     "     border-left-color: darkgray;\n"
                                     "     border-left-style: solid; /* just a single line */\n"
                                     "     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
                                     "     border-bottom-right-radius: 3px;\n"
                                     "     padding: 1px 0px 1px 10px;\n"
                                     " }\n"
                                     "\n"
                                     "QComboBox::down-arrow, QSpinBox::down-arrow, QTimeEdit::down-arrow, QDateEdit::down-arrow\n"
                                     "{\n"
                                     "     width: 7px;\n"
                                     "     height: 5px;\n"
                                     "}")
        self.choiceBox.setObjectName("choiceBox")
        self.choiceBox.addItem("")
        self.choiceBox.addItem("")
        self.choiceBox.addItem("")
        self.choiceBox.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.buttonEncrypt.setText(_translate("MainWindow", "encrypt"))
        self.buttonDecrypt.setText(_translate("MainWindow", "decrypt"))
        self.keyLine.setPlaceholderText(_translate("MainWindow", "key"))
        self.testForAction.setPlaceholderText(_translate("MainWindow", "text for action"))
        self.choiceBox.setItemText(0, _translate("MainWindow", "caesar"))
        self.choiceBox.setItemText(1, _translate("MainWindow", "caesar_key"))
        self.choiceBox.setItemText(2, _translate("MainWindow", "affine"))
        self.choiceBox.setItemText(3, _translate("MainWindow", "trisemus"))
