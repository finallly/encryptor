from PyQt5 import QtWidgets


class ErrorWindow(QtWidgets.QMessageBox):

    def __init__(self, parent=None):
        super(ErrorWindow, self).__init__(parent)

    def popup_window(self, state, text, icon=None):
        self.setWindowTitle(state)  # TODO: need constant access to state types
        self.setText(text)
        self.setIcon(self.Warning)
        self.exec()
