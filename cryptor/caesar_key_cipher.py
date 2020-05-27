from .parentFile import Cipher
from errorHandler import ErrorWindow


class CaesarKeyCipher(Cipher):

    def __init__(self, text, keyword=None):
        super(CaesarKeyCipher, self).__init__(text, keyword)
        self.key = sum([ord(symbol) for symbol in keyword]) if keyword is not None else int(False)
        self.symbols = [symbol for symbol in self.text]

    def encrypt(self) -> str:
        """
        this method uses caesar with key method of encryption
        :return: encrypted text
        """
        self.endText = ''.join([chr(ord(symbol) + self.key) for symbol in self.symbols])
        return self.endText

    def decrypt(self) -> str:
        """
        this method uses caesar with key method of encryption
        :return: decrypted text
        """
        try:
            self.endText = ''.join([chr(ord(symbol) - self.key) for symbol in self.symbols])
        except ValueError:
            ErrorWindow().popup_window('value error', 'you can only encode this message')
        return self.endText
