import sys
from interface import FormWindow
from PyQt5 import QtWidgets

if __name__ == '__main__':
    application = QtWidgets.QApplication(sys.argv)
    window = FormWindow()
    window.show()
    sys.exit(application.exec_())


# from utilites import Helpers
#
# x = Helpers.lambda_dict.get('trisemus')('text', 'key')
# print(x.encrypt())
# y = Helpers.lambda_dict.get('trisemus')('wbBw', 'key')
# print(y.decrypt())