import unittest
from Fizz_buzz import fizz_buzz


class TestFizzBuzz(unittest.TestCase):

    def test_affiche_retourne_chaine(self):
        fb = fizz_buzz()
        resultat = fb.affiche()
        self.assertEqual(resultat, "")
if __name__ == "__main__":
    unittest.main()
