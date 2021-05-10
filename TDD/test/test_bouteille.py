"""
Test du module bouteille.py
"""
import unittest
# Permet de définir le chemin relatif pour importer le répertoire parent
import sys
sys.path.append('..')

# Importation de la class à tester
from src.bouteille import Bouteille


class TestBouteille(unittest.TestCase):

    # Exemple avec un appel des données dans chaque test
    # def test_bouteille_is_created(self):
    #    b = Bouteille("Cannette", 330, 150)
    #    self.assertIsInstance(b, Bouteille)

    # def test_quantity_max_is_positive(self):
    #    b = Bouteille("Cannette", 330)
    #    self.assertGreater(b.quantity_max, 0)

    # Méthode permettant de préparer des données pour tout les test
    def setUp(self):
        self.b = Bouteille("Cannette", 330, 150)

    # Pour reinitialise les données entre chaque tests :
    def tearDown(self):
        self.b.quantity = 0
        self.b.durability = 150

    def test_bouteille_is_created(self):
        self.assertIsInstance(self.b, Bouteille)

    def test_quantity_max_is_positive(self):
        self.assertGreater(self.b.quantity_max, 0)

    def test_quantity_is_zero(self):
        self.assertEqual(self.b.quantity, 0)

    def test_last_drink(self):
        self.b.quantity = 2
        self.b.durability = 1
        self.assertTrue(self.b.drink(1))

    def test_broken_when_to_drink(self):
        self.b.quantity = 2
        self.b.durability = 0
        self.assertFalse(self.b.drink(1))

    def test_drink(self):
        self.b.quantity = 2
        self.assertTrue(self.b.drink(1))

    def test_drink_full_capacity(self):
        self.b.quantity = 330
        self.assertFalse(self.b.drink(100))

    def test_drink_over_capacity(self):
        self.b.quantity = 10
        self.assertFalse(self.b.drink(100))

# Permet d'exécuter directement depuis le fichier
if __name__ == '__main__':
    unittest.main()
