import unittest
from Cryptage import Cryptage

class TestCryptage(unittest.TestCase):

    def test_crypt_simple(self):
        c = Cryptage()
        resultat = c.crypt("abc")
        self.assertEqual(resultat, "bcd")  # chaque lettre décalée de 1

if __name__ == "__main__":
    unittest.main()
