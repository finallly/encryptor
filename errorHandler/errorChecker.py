from utilites.consts import Consts


class ErrorChecker:

    def __init__(self, cipher, text, key=None):
        self.currentCipher = cipher
        self.text = text
        self.key = key

    def check(self) -> dict:
        self.answer_dict = {'flag': None, 'title': None, 'text': None}

        if self.text == str():
            self.answer_dict['flag'] = False
            self.answer_dict['title'] = 'input error'
            self.answer_dict['text'] = 'your must enter the text first'
            return self.answer_dict

        if self.currentCipher == 'trisemus':

            self.key_check = self.key.isalpha()
            self.alphabet = Consts.const_dict.get('alphabet_lower') + Consts.const_dict.get('alphabet_higher') + ' '
            self.text_check = all([letter in self.alphabet for letter in self.text])

            if self.key_check and self.text_check:

                self.answer_dict['flag'] = True

            elif not self.key_check and self.text_check:

                self.answer_dict['flag'] = False
                self.answer_dict['title'] = 'key error'
                self.answer_dict['text'] = 'key should only include lower or upper case letters'

            elif not self.text_check and self.key_check:

                self.answer_dict['flag'] = False
                self.answer_dict['title'] = 'text error'
                self.answer_dict['text'] = 'text should only include lower or upper case letters and spaces'

            else:

                self.answer_dict['flag'] = False
                self.answer_dict['title'] = 'fill error'
                self.answer_dict[
                    'text'] = 'key should only include lower or upper case letters while text can also include spaces'

        if self.currentCipher == 'caesar':
            self.answer_dict['flag'] = True

        if self.currentCipher == 'caesar_key':

            if self.key != str():

                self.answer_dict['flag'] = True
            else:
                self.answer_dict['flag'] = False
                self.answer_dict['title'] = 'input error'
                self.answer_dict['text'] = 'your must enter the key for caesar_key cipher'

        if self.currentCipher == 'affine':
            if self.text.isalpha():
                self.answer_dict['flag'] = True
            else:
                self.answer_dict['flag'] = False
                self.answer_dict['title'] = 'text error'
                self.answer_dict['text'] = 'text should only include lower or upper case letters and spaces'

        return self.answer_dict
