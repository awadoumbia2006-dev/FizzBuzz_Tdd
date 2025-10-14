class fizz_buzz:
    def __init__(self):
        pass

    def affiche(self):
        resultat = ""
        for i in range(1, 101):  # on génère tous les nombres
            resultat += str(i)
        return resultat
