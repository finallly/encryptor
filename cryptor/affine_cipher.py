from .parentFile import Cipher


class AffineCipher(Cipher):

    def __init__(self, text, keyword=None):
        super(AffineCipher, self).__init__(text, keyword)
        self.endText = str()

    def encrypt(self):
        return self.endText

    def decrypt(self):
        return self.endText
