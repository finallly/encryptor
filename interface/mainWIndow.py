from .form import FrontWindow
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

        self.choiseBox.textActivated.connect(self.flag_checker)
        self.keyLine.editingFinished.connect(self.key_checker)

        self.setWindowTitle('something will be here')

        # TODO: add name here

    def encrypt_button(self):
        self.text = self.testForAction.toPlainText()
        self.instance = Helpers.lambda_dict.get(self.choiseBox.currentText())(self.text, keyword=self.keyLine.text())
        self.resultText.setText(self.instance.encrypt())

    def decrypt_button(self):
        self.text = self.testForAction.toPlainText()
        self.instance = Helpers.lambda_dict.get(self.choiseBox.currentText())(self.text, keyword=self.keyLine.text())
        self.resultText.setText(self.instance.decrypt())

    def flag_checker(self):
        if Consts.const_dict.get(self.choiseBox.currentText()):
            self.keyLine.show()
        else:
            self.keyLine.hide()

    def key_checker(self):
        self.key = self.keyLine.text()
