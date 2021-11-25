import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)

    def test_ostoskoriin_lisataan_tuote(self):
        t = Tuote("maito", 5)
        self.kori.lisaa_tuote(t)
        self.assertEqual(self.kori.hinta(), 5)
