import sys
from interface import FormWindow
from PyQt5 import QtWidgets

if __name__ == '__main__':
    application = QtWidgets.QApplication(sys.argv)
    window = FormWindow()
    window.show()
    sys.exit(application.exec_())

# lst1, lst2 = [], []
# for i in range(52):
#     lst1.append(i)
#     lst2.append((49 * i + 43) % 52)
#
# print(lst1)
# print(lst2)
# print(len(set(lst2)) == len(lst2))
# from utilites import consts
#
#
# stri = consts.Consts.const_dict.get('alphabet_lower') + consts.Consts.const_dict.get('alphabet_higher')
# print(dict(enumerate(stri)))
