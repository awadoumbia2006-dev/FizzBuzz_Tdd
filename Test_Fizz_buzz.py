import unittest
from Fizz_buzz import fizz_buzz

class TestFizzBuzz(unittest.TestCase):
    def test_affiche_existe(self):
        fb = fizz_buzz()
        # On s'attend à ce que la méthode affiche() existe
        # mais pour l'instant, elle n'existe pas → le test doit échouer
        with self.assertRaises(AttributeError):
            fb.affiche()
