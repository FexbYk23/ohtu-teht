import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(len(self.kori.ostokset()), 0)

    def test_ostoskoriin_lisataan_tuote(self):
        t = Tuote("maito", 5)
        self.kori.lisaa_tuote(t)
        self.assertEqual(self.kori.hinta(), 5)

    def test_ostoskorista_poistetaan_tuote(self):
        t = Tuote("maito", 5)
        self.kori.lisaa_tuote(t)
        self.kori.poista_tuote(t)
        self.assertEqual(self.kori.hinta(), 0)
    
    def test_saman_tuotteen_lisays(self):
        t = Tuote("piimä", 5)
        self.kori.lisaa_tuote(t)
        self.kori.lisaa_tuote(t)
        self.assertEqual(len(self.kori.ostokset()), 1)
        self.assertEqual(self.kori.ostokset()[0].lukumaara(), 2)

    def test_tavaroiden_maara_korissa(self):
        t = Tuote("piimä", 5)
        self.kori.lisaa_tuote(t)
        self.kori.lisaa_tuote(t)
        self.kori.lisaa_tuote(Tuote("maito", 5))
        
        self.assertEqual(self.kori.tavaroita_korissa(), 3)


