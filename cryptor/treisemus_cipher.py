from .parentFile import Cipher
from utilites.consts import Consts


class TrisemusCipher(Cipher):

    def __init__(self, text, keyword):
        super(TrisemusCipher, self).__init__(text, keyword)
        self.table = self.table_maker(self.key)
        self.key = keyword

    def encrypt(self) -> str:
        self.endText = str()
        for letter in self.text:
            indexes = self.indexer(self.table, letter)
            if indexes[0] != len(self.table) - 1 and indexes[0] + 1 != '0':
                self.endText += self.table[indexes[0] + 1][indexes[1]]
            else:
                self.endText += self.table[0][indexes[1]]
        return self.endText

    def decrypt(self) -> str:
        self.endText = str()
        for letter in self.text:
            indexes = self.indexer(self.table, letter)
            if indexes[0] != int(False):
                self.endText += self.table[indexes[0] - 1][indexes[1]]
            elif indexes[0] == int(False) and len(self.table) - 1 != '0':
                self.endText += self.table[len(self.table) - 1][indexes[1]]
            else:
                self.endText += self.table[len(self.table) - 2][indexes[1]]
        return self.endText

    @staticmethod
    def indexer(table, letter) -> tuple:
        for i in range(len(table)):
            for j in range(len(table[0])):
                if table[i][j] == letter:
                    return i, j

    @staticmethod
    def table_maker(key) -> list:
        space_flag = False
        flag, lst, seen, length, stroke = key[0].islower(), [], set(), len(key), str()
        for letter in key:
            if letter not in seen:
                stroke += letter
                seen.add(letter)
        if flag:
            for letter in Consts.const_dict.get('alphabet_lower'):
                if letter not in seen:
                    stroke += letter
                    seen.add(letter)
            for letter in Consts.const_dict.get('alphabet_higher'):
                if letter not in seen:
                    stroke += letter
                    seen.add(letter)
        else:
            for letter in Consts.const_dict.get('alphabet_higher'):
                if letter not in seen:
                    stroke += letter
                    seen.add(letter)
            for letter in Consts.const_dict.get('alphabet_lower'):
                if letter not in seen:
                    stroke += letter
                    seen.add(letter)
        for i in range(0, len(stroke), length):
            lts = []
            for j in range(i, i + length):
                try:
                    lts.append(stroke[j])
                except IndexError:
                    if not space_flag:
                        lts.append(' ')
                    else:
                        lts.append('0')
            lst.append(lts)
        if len(key) in (2, 4, 13, 26):
            lst.append([' ', 0, 0, 0])
        return lst
