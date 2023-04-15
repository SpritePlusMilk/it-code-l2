import random
import pyperclip

class Password:
    def __init__(self, length: int):
        self.password = Password.generate(length)
        pyperclip.copy(self.password)

    def generate(x: int):
        pword = ""
        for i in range(x):
            pword += str(chr(random.randint(33, 127)))
        return pword
sas = Password(9)