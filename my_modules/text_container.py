import string


class TextContainer():
    """ A class for getting different kinds of information about a text"""

    def __init__(self, txt):
        self.txt = txt

    def count_words(self):
        print(len(self.txt.split()))

    def count_chars(self):
        print(len(self.txt))

    def count_letters(self):
        counter = 0
        for char in self.txt:
            if char in string.ascii_letters:
                counter += 1
        print(counter)

    def remove_punctuation(self):
        print(self.txt.replace(string.punctuation, ''))


if __name__ == '__main__':
    txt = "Det her er en text! Den indeholder nogle punctuations. Fx. ? og @ og % osv."
    tc = TextContainer(txt)
    print('Antal ord i text : ')
    tc.count_words()

    print('Antal chars i text : ')
    tc.count_chars()

    print('Antal ASCII bogstaver : ')
    tc.count_letters()

    print('Teksten uden punctuations : ')
    tc.remove_punctuation()
