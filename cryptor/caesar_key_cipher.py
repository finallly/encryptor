from .parentFile import Cipher


class CaesarKeyCipher(Cipher):

    def __init__(self, text, keyword=None):
        super(CaesarKeyCipher, self).__init__(text, keyword)
        self.key = sum([ord(symbol) for symbol in keyword]) if keyword is not None else int(False)
        self.symbols = [symbol for symbol in self.text]

    def encrypt(self):
        self.endText = ''.join([chr(ord(symbol) + self.key) for symbol in self.symbols])
        return self.endText

    def decrypt(self):
        self.endText = ''.join([chr(ord(symbol) - self.key) for symbol in self.symbols])
        return self.endText
