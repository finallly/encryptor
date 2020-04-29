from .parentFile import Cipher


class CaesarCipher(Cipher):

    def __init__(self, text):
        super(CaesarCipher, self).__init__(text)
        self.symbols = [symbol for symbol in self.text]

    def encrypt(self):
        self.endText = ''.join([chr(ord(symbol) + 3) for symbol in self.symbols])
        return self.endText

    def decrypt(self):
        self.endText = ''.join([chr(ord(symbol) - 3) for symbol in self.symbols])
        return self.endText
