import string

class Cryptage:
    def __init__(self):
        # Table de caractères
        self.caracteres = string.ascii_letters + string.punctuation + string.digits + " "

    def crypt(self, message, pas=1):
        resultat = ""
        for char in message:
            if char in self.caracteres:
                index = self.caracteres.index(char)
                resultat += self.caracteres[(index + pas) % len(self.caracteres)]
            else:
                resultat += char  # si caractère non trouvé (sécurité)
        
        # Ajoute le pas seulement s’il a été fourni explicitement
        if pas != 1:
            resultat += str(pas)
        return resultat

    def decrypt(self, message):
        # Récupère le pas à la fin si c’est un chiffre
        if message[-1].isdigit():
            pas = int(message[-1])
            message = message[:-1]
        else:
            pas = 1

        resultat = ""
        for char in message:
            if char in self.caracteres:
                index = self.caracteres.index(char)
                resultat += self.caracteres[(index - pas) % len(self.caracteres)]
            else:
                resultat += char
        return resultat
