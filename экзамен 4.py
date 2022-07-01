import string
class Alphabet:
    def __init__(self,lang,letters):
        self.lang = lang #язык
        self.letters = letters  #список букв

    def print(self):
        print(self.letters)  #буквы алфавита

    def letters_num(self):
        print(len(self.letters)) #указывам кол-во букв в алфавите



class EngAlphabet(Alphabet):

    __letters_num = 26

    def __init__(self):
        super().__init__('En', string.ascii_uppercase )

    def is_en_letters(self, letter): #проверяем есть ли указаная буква в алфавите
        if letter.upper() in self.letters:
            return True
        else:
            return False

    def letters_num(self):
        return EngAlphabet.__letters_num

    @staticmethod
    def example():
        print('English example: Hello, World') # риемр английского текста


object_EngAlphabet = EngAlphabet()
object_EngAlphabet.print()
print(object_EngAlphabet.letters_num())
print(object_EngAlphabet.is_en_letters('F'))
print(object_EngAlphabet.is_en_letters('Щ'))
print(object_EngAlphabet.example())



