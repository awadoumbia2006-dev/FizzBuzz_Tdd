import string

class Cryptage:
    def __init__(self):
        self.caracteres = string.ascii_letters + string.punctuation + string.digits + " "


    def crypt(self, message, pas=1):
        resultat = ""
        for char in message:
            index = self.caracteres.index(char)
            resultat += self.caracteres[(index + pas) % len(self.caracteres)]

        # N’ajoute le pas à la fin que si l’utilisateur l’a fourni explicitement
        if pas != 1:
            resultat += str(pas)

        return resultat


