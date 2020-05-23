from PyQt5 import QtWidgets


class ErrorWindow(QtWidgets.QMessageBox):

    def __init__(self, parent=None):
        super(ErrorWindow, self).__init__(parent)

    def popup_window(self, state: str, text: str, icon=None) -> None:
        """
        this method pops up the error window
        :param state: name of error
        :param text: error message
        """
        self.setWindowTitle(state)
        self.setText(text)
        self.setIcon(self.Warning)
        self.exec()
