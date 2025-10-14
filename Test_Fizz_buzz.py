import unittest
from Fizz_buzz import fizz_buzz


class TestFizzBuzz(unittest.TestCase):

    def test_multiples_de_3(self):
        fb = fizz_buzz()
        resultat = fb.affiche()
    # 3 est un multiple de 3 → doit être remplacé
        self.assertIn("Fizz", resultat)
        #self.assertNotIn("3", resultat)

        self.assertEqual(fb.affiche(),"12Fizz4BuzzFizz78FizzBuzz11Fizz1314FrisBee1617" \
        "Fizz19BuzzFizz2223FizzBuzz26Fizz2829FrisBee3132Fizz34BuzzFizz3738FizzBuzz41" \
        "Fizz4344FrisBee4647Fizz49BuzzFizz5253FizzBuzz56Fizz5859FrisBee6162Fizz64BuzzFizz" \
        "6768FizzBuzz71Fizz7374FrisBee7677Fizz79BuzzFizz8283FizzBuzz86Fizz8889FrisBee9192" \
        "Fizz94BuzzFizz9798FizzBuzz")

if __name__ == "__main__":
    unittest.main()
