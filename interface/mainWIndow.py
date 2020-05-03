from .form import FrontWindow
from errorHandler import ErrorWindow, ErrorChecker
from utilites import Helpers, Consts

from PyQt5 import QtWidgets


class FormWindow(QtWidgets.QMainWindow, FrontWindow):

    def __init__(self, parent=None):
        super(FormWindow, self).__init__(parent)

        self.setup_ui(self)

        self.buttonEncrypt.clicked.connect(self.encrypt_button)
        self.buttonDecrypt.clicked.connect(self.decrypt_button)

        self.resultText.setReadOnly(True)
        self.keyLine.hide()

        self.keyLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.keyLine.setMaxLength(14)

        self.choiseBox.textActivated.connect(self.flag_checker)
        self.keyLine.editingFinished.connect(self.key_checker)

        self.setWindowTitle('crypto')

        self.key = str()

        # TODO: add name here

    def encrypt_button(self):
        self.text = self.testForAction.toPlainText()
        if self.error_checker():
            self.instance = Helpers.lambda_dict.get(self.choiseBox.currentText())(self.text, keyword=self.key)
            self.resultText.setText(self.instance.encrypt())

    def decrypt_button(self):
        self.text = self.testForAction.toPlainText()
        if self.error_checker():
            self.instance = Helpers.lambda_dict.get(self.choiseBox.currentText())(self.text, keyword=self.key)
            self.resultText.setText(self.instance.decrypt())

    def flag_checker(self):
        if Consts.cipher_flags.get(self.choiseBox.currentText()):
            self.keyLine.show()
        else:
            self.keyLine.hide()

    def key_checker(self):
        self.key = self.keyLine.text()

    def error_checker(self):
        self.answer = ErrorChecker(self.choiseBox.currentText(), self.text, self.key).check()
        if self.answer.get('flag'):
            return True
        else:
            ErrorWindow().popup_window(self.answer.get('title'), self.answer.get('text'))
            return False
