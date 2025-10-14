import unittest
from Fizz_buzz import fizz_buzz


class TestFizzBuzz(unittest.TestCase):

    def test_affiche_commence_par_1(self):
        fb = fizz_buzz()
        resultat = fb.affiche()
        self.assertTrue(resultat.startswith("1"))


if __name__ == "__main__":
    unittest.main()
