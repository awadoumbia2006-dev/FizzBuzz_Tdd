import unittest
from Fizz_buzz import fizz_buzz


class TestFizzBuzz(unittest.TestCase):

    def test_affiche_entre_deux_valeurs(self):
        fb = fizz_buzz()
        resultat = fb.affiche(5, 10)
        attendu = "BuzzFizz78FizzBuzz"
        self.assertEqual(resultat, attendu)


if __name__ == "__main__":
    unittest.main()
