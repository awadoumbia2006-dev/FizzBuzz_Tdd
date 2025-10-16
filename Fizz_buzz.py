class fizz_buzz:
    def __init__(self):
        pass

    def affiche(self, n1=1, n2=100):  # ✅ accepte maintenant 2 paramètres
        resultat = ""
        for i in range(n1, n2 + 1):
            if i % 15 == 0:
                resultat += "FrisBee"
            elif i % 3 == 0:
                resultat += "Fizz"
            elif i % 5 == 0:
                resultat += "Buzz"
            else:
                resultat += str(i)
        return resultat
