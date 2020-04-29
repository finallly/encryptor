from .form import FrontWindow
from PyQt5 import QtWidgets


class FormWindow(QtWidgets.QMainWindow, FrontWindow):

    def __init__(self, parent=None):
        super(FormWindow, self).__init__(parent)

        self.setupui(self)

        # TODO: add button bindings
