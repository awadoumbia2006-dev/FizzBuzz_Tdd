import unittest
from Cryptage import Cryptage

class TestCryptage(unittest.TestCase):

    def test_crypt_simple(self):
        c = Cryptage()
        resultat = c.crypt("abc")
        self.assertEqual(resultat, "bcd")  # chaque lettre décalée de 1


    def test_crypt_avec_pas(self):
        c = Cryptage()  # création de l'objet c
        resultat = c.crypt("abc", 2)
        self.assertEqual(resultat, "cde2")  # décalé de 2 + ajout du pas
    def test_decrypt(self):
        c = Cryptage()
        message_crypte = c.crypt("abc", 3)  # => "def3"
        resultat = c.decrypt(message_crypte)
        self.assertEqual(resultat, "abc")
    

if __name__ == "__main__":
     unittest.main()