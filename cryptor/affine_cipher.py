from .parentFile import Cipher
from utilites.consts import Consts


class AffineCipher(Cipher):

    def __init__(self, text, keyword=None):
        super(AffineCipher, self).__init__(text, keyword)
        self.endText = str()
        self.alphabet = Consts.const_dict.get('alphabet_lower') + Consts.const_dict.get('alphabet_higher') + ' '

    def encrypt(self):
        self.base_dict = dict(enumerate(self.alphabet))
        self.crypto_dict = dict([(v, k) for k, v in enumerate(self.alphabet)])
        self.end_dict = {}

        for k, v in dict(enumerate([(17 * i + 23) % 53 for i in range(53)])).items():
            self.end_dict[k] = self.base_dict.get(v)

        for letter in self.text:
            self.endText += self.end_dict.get(self.crypto_dict.get(letter))

        return self.endText

    def decrypt(self):
        self.base_dict = dict(enumerate(self.alphabet))
        self.crypto_dict = dict([(v, k) for k, v in enumerate(self.alphabet)])
        self.end_dict = {}

        for k, v in dict(enumerate([(17 * i + 23) % 53 for i in range(53)])).items():
            self.end_dict[self.base_dict.get(v)] = k

        for letter in self.text:
            self.endText += self.base_dict.get(self.end_dict.get(letter))

        return self.endText
