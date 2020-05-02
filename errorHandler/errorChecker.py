from utilites.consts import Consts


class ErrorChecker:

    def __init__(self, cipher, text, key=None):
        self.currentCipher = cipher
        self.text = text
        self.key = key

    def check(self):
        self.answer_dict = {'flag': None, 'title': None, 'text': None}
        if self.currentCipher == 'trisemus':
            self.key_check = self.key.isalpha()
            self.alphabet = Consts.const_dict.get('alphabet_lower') + Consts.const_dict.get('alphabet_higher') + ' '
            self.text_check = all([letter in self.alphabet for letter in self.text])
            if self.key_check and self.text_check:
                self.answer_dict['flag'] = True
                return self.answer_dict
            elif not self.key_check and self.text_check:
                self.answer_dict['flag'] = False
                self.answer_dict['title'] = 'key error'
                self.answer_dict['text'] = 'key should only include lower or upper case letters'
                return self.answer_dict
            elif not self.text_check and self.key_check:
                self.answer_dict['flag'] = False
                self.answer_dict['title'] = 'text error'
                self.answer_dict['text'] = 'text should only include lower or upper case letters and spaces'
                return self.answer_dict
            else:
                self.answer_dict['flag'] = False
                self.answer_dict['title'] = 'fill error'
                self.answer_dict[
                    'text'] = 'key should only include lower or upper case letters while text can also include spaces'
                return self.answer_dict
