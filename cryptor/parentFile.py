class Cipher(object):

    def __init__(self, text, keyword=None):
        self.text = text
        self.key = keyword
        self.endText = str()

    def encrypt(self):
        return self.endText

    def decrypt(self):
        return self.endText
