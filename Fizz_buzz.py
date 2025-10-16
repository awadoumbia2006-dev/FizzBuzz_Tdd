class fizz_buzz:
    def __init__(self):
        pass

    def get_resultat(self, n):
        resultat = ""
        for i in range(1, n + 1):
            if i % 15 == 0:
                resultat += "FrisBee"
            elif i % 3 == 0:
                resultat += "Fizz"
            elif i % 5 == 0:
                resultat += "Buzz"
            else:
                resultat += str(i)
        return resultat

    def affiche(self, n=100):
        print(self.get_resultat(n))
        return self.get_resultat(n)
