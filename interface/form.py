# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets


class FrontWindow(object):
    def setup_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.buttonEncrypt = QtWidgets.QPushButton(self.centralwidget)
        self.buttonEncrypt.setGeometry(QtCore.QRect(10, 280, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.buttonEncrypt.setFont(font)
        self.buttonEncrypt.setStyleSheet("QPushButton {\n"
                                         "  background-color: rgb(215, 215, 215);\n"
                                         "  border: 1px solid gray;\n"
                                         "}\n"
                                         "QPushButton:pressed {\n"
                                         "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                         "                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
                                         "}")
        self.buttonEncrypt.setObjectName("buttonEncrypt")
        self.buttonDecrypt = QtWidgets.QPushButton(self.centralwidget)
        self.buttonDecrypt.setGeometry(QtCore.QRect(150, 280, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.buttonDecrypt.setFont(font)
        self.buttonDecrypt.setStyleSheet("QPushButton {\n"
                                         "  background-color: rgb(215, 215, 215);\n"
                                         "  border: 1px solid gray;\n"
                                         "}\n"
                                         "QPushButton:pressed {\n"
                                         "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                         "                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
                                         "}")
        self.buttonDecrypt.setObjectName("buttonDecrypt")
        self.keyLine = QtWidgets.QLineEdit(self.centralwidget)
        self.keyLine.setGeometry(QtCore.QRect(280, 280, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.keyLine.setFont(font)
        self.keyLine.setStyleSheet("  background-color: white;\n"
                                   " border: 1px solid gray;")
        self.keyLine.setObjectName("keyLine")
        self.choiseBox = QtWidgets.QComboBox(self.centralwidget)
        self.choiseBox.setGeometry(QtCore.QRect(440, 280, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.choiseBox.setFont(font)
        self.choiseBox.setStyleSheet(" background-color: rgb(215, 215, 215);\n"
                                     "  border: 1px solid gray;")
        self.choiseBox.setObjectName("choiseBox")
        self.choiseBox.addItem("")
        self.choiseBox.addItem("")
        self.choiseBox.addItem("")
        self.choiseBox.addItem("")
        self.testForAction = QtWidgets.QTextEdit(self.centralwidget)
        self.testForAction.setGeometry(QtCore.QRect(10, 10, 781, 261))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.testForAction.setFont(font)
        self.testForAction.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.testForAction.setObjectName("testForAction")
        self.resultText = QtWidgets.QTextEdit(self.centralwidget)
        self.resultText.setGeometry(QtCore.QRect(10, 320, 781, 251))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.resultText.setFont(font)
        self.resultText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.resultText.setObjectName("resultText")
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
        self.choiseBox.setItemText(0, _translate("MainWindow", "caesar"))
        self.choiseBox.setItemText(1, _translate("MainWindow", "caesar_key"))
        self.choiseBox.setItemText(2, _translate("MainWindow", "affine"))
        self.choiseBox.setItemText(3, _translate("MainWindow", "trisemus"))
        self.testForAction.setPlaceholderText(_translate("MainWindow", "text for action"))
