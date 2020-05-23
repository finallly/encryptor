from .form import FrontWindow
from errorHandler import ErrorWindow, ErrorChecker
from utilites import Helpers, Consts

from PyQt5 import QtWidgets


class FormWindow(QtWidgets.QMainWindow, FrontWindow):

    def __init__(self, parent=None):
        super(FormWindow, self).__init__(parent)

        # activation of the form
        self.setup_ui(self)

        # button bindings
        self.buttonEncrypt.clicked.connect(self.encrypt_button)
        self.buttonDecrypt.clicked.connect(self.decrypt_button)

        # keyLine settings
        self.resultText.setReadOnly(True)
        self.keyLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.keyLine.editingFinished.connect(self.key_checker)
        self.keyLine.setMaxLength(14)
        self.keyLine.hide()

        # choiceBox flag
        self.choiceBox.textActivated.connect(self.flag_checker)

        # title
        self.setWindowTitle('crypto')

        self.key = str()

    def encrypt_button(self) -> None:
        """
        this method initialize 'encrypt' button
        :return: None
        """
        self.text = self.testForAction.toPlainText()
        if self.error_checker():
            self.instance = Helpers.lambda_dict.get(self.choiceBox.currentText())(self.text, keyword=self.key)
            self.resultText.setText(self.instance.encrypt())

    def decrypt_button(self) -> None:
        """
        this method initialize 'decrypt' button
        """
        self.text = self.testForAction.toPlainText()
        if self.error_checker():
            self.instance = Helpers.lambda_dict.get(self.choiceBox.currentText())(self.text, keyword=self.key)
            self.resultText.setText(self.instance.decrypt())

    def flag_checker(self) -> None:
        """
        this method checks if cipher need the keyLine
        """
        if Consts.cipher_flags.get(self.choiceBox.currentText()):
            self.keyLine.show()
        else:
            self.keyLine.hide()

    def key_checker(self) -> None:
        """
        this method defined the key
        """
        self.key = self.keyLine.text()

    def error_checker(self) -> bool:
        """
         this method handles error in text or keys
        """
        self.answer = ErrorChecker(self.choiceBox.currentText(), self.text, self.key).check()
        if self.answer.get('flag'):
            return True
        else:
            ErrorWindow().popup_window(self.answer.get('title'), self.answer.get('text'))
            return False
