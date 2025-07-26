import random
import string
from datetime import datetime

class WordlistGenerator:
    def __init__(self, name='', dob='', pet=''):
        self.name = name
        self.dob = dob
        self.pet = pet
        self.wordlist = []

    def leetspeak(self, word):
        table = str.maketrans("aAeEiIoOsStT", "443311005577")
        return word.translate(table)

    def append_years(self, word):
        current_year = datetime.now().year
        return [f"{word}{y}" for y in range(current_year-5, current_year+1)]

    def generate_custom_words(self):
        base_words = filter(None, [self.name, self.pet, self.dob])
        for word in base_words:
            word = word.lower()
            self.wordlist.append(word)
            self.wordlist.append(self.leetspeak(word))
            self.wordlist.extend(self.append_years(word))

    def generate_common_passwords(self):
        self.wordlist.extend([
            "password", "123456", "admin", "letmein", "qwerty", "welcome", "test123"
        ])

    def generate_random_passwords(self, count=50):
        for _ in range(count):
            length = random.randint(8, 12)
            chars = string.ascii_letters + string.digits + string.punctuation
            self.wordlist.append(''.join(random.choices(chars, k=length)))

    def generate_wordlist(self):
        self.generate_custom_words()
        self.generate_common_passwords()
        self.generate_random_passwords()
        return list(set(self.wordlist))

    def export_wordlist(self, filename='wordlist.txt'):
        with open(filename, 'w') as f:
            for word in self.wordlist:
                f.write(word + '\n')