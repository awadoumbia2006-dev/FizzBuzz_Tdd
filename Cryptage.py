import string

class Cryptage:
    def __init__(self):
        self.caracteres = string.ascii_letters + string.punctuation + string.digits + " "


    def crypt(self, message):
        resultat = ""
        for char in message:
            index = self.caracteres.index(char)
            resultat += self.caracteres[(index + 1) % len(self.caracteres)]
        return resultat
