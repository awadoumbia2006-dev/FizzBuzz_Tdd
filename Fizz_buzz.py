class fizz_buzz:
    def __init__(self):
        pass


    def affiche(self):
        resultat = ""
        for i in range(1, 101):
            if i % 15 == 0:
                resultat += "FrisBee"
            elif i % 3 == 0:
                resultat += "Fizz"
            elif i % 5 == 0:
                resultat += "Buzz"
            else:
                resultat += str(i)
        return resultat
