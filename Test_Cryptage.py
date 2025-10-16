import unittest
from cryptage import Cryptage

class TestCryptage(unittest.TestCase):

    def test_crypt_simple(self):
        c = Cryptage()
        resultat = c.crypt("abc")
        self.assertEqual(resultat, "bcd")  # chaque lettre décalée de 1
