from cryptor import CaesarCipher, CaesarKeyCipher


class Helpers:
    lambda_dict = {
        'caesar': lambda obj: CaesarCipher(obj),
        'caesar_key': lambda obj: CaesarKeyCipher(obj)
    }
