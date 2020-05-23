class Cipher(object):

    def __init__(self, text: str, keyword=None):
        self.text = text
        self.key = keyword
        self.endText = str()

    def encrypt(self) -> str:
        return self.endText

    def decrypt(self) -> str:
        return self.endText
