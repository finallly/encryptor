from .form import FrontWindow
from utilites import Helpers

from PyQt5 import QtWidgets


class FormWindow(QtWidgets.QMainWindow, FrontWindow):

    def __init__(self, parent=None):
        super(FormWindow, self).__init__(parent)

        self.setup_ui(self)

        self.buttonEncrypt.clicked.connect(self.encrypt_button)
        self.buttonDecrypt.clicked.connect(self.decrypt_button)
        self.keyLine.hide()
        self.resultText.setReadOnly(True)

        self.setWindowTitle('something will be here')

        # TODO: add name here

    def encrypt_button(self):

        self.text = self.testForAction.toPlainText()
        self.instance = Helpers.lambda_dict.get('{}'.format(self.choiseBox.currentText()))
        self.endText = self.instance(self.text).encrypt()
        self.resultText.setText(self.endText)

    def decrypt_button(self):
        self.text = self.testForAction.toPlainText()
        self.instance = Helpers.lambda_dict.get('{}'.format(self.choiseBox.currentText()))
        self.endText = self.instance(self.text).decrypt()
        self.resultText.setText(self.endText)
