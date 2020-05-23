from .parentFile import Cipher


class CaesarCipher(Cipher):

    def __init__(self, text, keyword=None):
        super(CaesarCipher, self).__init__(text, keyword)
        self.symbols = [symbol for symbol in self.text]

    def encrypt(self) -> str:
        """
        this method uses caesar method of encryption
        :return: encrypted text
        """
        self.endText = ''.join([chr(ord(symbol) + 3) for symbol in self.symbols])
        return self.endText

    def decrypt(self) -> str:
        """
        this method uses caesar method of encryption
        :return: decrypted text
        """
        self.endText = ''.join([chr(ord(symbol) - 3) for symbol in self.symbols])
        return self.endText
