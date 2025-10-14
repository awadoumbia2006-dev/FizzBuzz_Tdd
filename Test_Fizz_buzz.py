import unittest
from Fizz_buzz import fizz_buzz


class TestFizzBuzz(unittest.TestCase):

    def test_multiples_de_3(self):
        fb = fizz_buzz()
        resultat = fb.affiche()
    # 3 est un multiple de 3 → doit être remplacé
        self.assertIn("Fizz", resultat)
        #self.assertNotIn("3", resultat)

        self.assertEqual(fb.affiche(),"12Fizz4BuzzFizz78FizzBuzz11Fizz1314FrisBee")

if __name__ == "__main__":
    unittest.main()
