import sys
from interface import FormWindow
from PyQt5 import QtWidgets

if __name__ == '__main__':
    application = QtWidgets.QApplication(sys.argv)
    window = FormWindow()
    window.show()
    sys.exit(application.exec_())
