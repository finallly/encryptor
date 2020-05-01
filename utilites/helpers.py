from cryptor import CaesarCipher, CaesarKeyCipher, AffineCipher, TrisemusCipher


class Helpers:
    lambda_dict = {
        'caesar': lambda text, keyword=None: CaesarCipher(text, keyword),
        'caesar_key': lambda text, keyword=None: CaesarKeyCipher(text, keyword),
        'affine': lambda text, keyword=None: AffineCipher(text, keyword),
        'trisemus': lambda text, keyword=None: TrisemusCipher(text, keyword)
    }
