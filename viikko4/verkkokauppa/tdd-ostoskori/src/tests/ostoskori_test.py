import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(len(self.kori.ostokset()), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

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


    def test_tavaroiden_maara_korissa_eri_tuote(self):
        t = Tuote("piimä", 5)
        self.kori.lisaa_tuote(t)
        self.kori.lisaa_tuote(t)
        self.kori.lisaa_tuote(Tuote("maito", 5))
        
        self.assertEqual(self.kori.tavaroita_korissa(), 3)

    def test_tavaroiden_maara_korissa_sama_tuote(self):
        t = Tuote("piimä", 5)
        self.kori.lisaa_tuote(t)
        self.kori.lisaa_tuote(t)
        
        self.assertEqual(self.kori.tavaroita_korissa(), 2)


    def test_tavaroiden_hinta_korissa_sama_tuote(self):
        t = Tuote("piimä", 5)
        self.kori.lisaa_tuote(t)
        self.kori.lisaa_tuote(t)
        self.kori.lisaa_tuote(t)
        
        self.assertEqual(self.kori.hinta(), 15)

    def test_tavaroiden_hinta_korissa_eri_tuote(self):
        t = Tuote("piimä", 5)
        self.kori.lisaa_tuote(t)
        self.kori.lisaa_tuote(Tuote("maito", 4))
        
        self.assertEqual(self.kori.hinta(), 9)

    
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostos(self):
        t = Tuote("piimä", 5)
        self.kori.lisaa_tuote(t)
        self.kori.lisaa_tuote(t)
        
        self.assertEqual(len(self.kori.ostokset()), 1)
 
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostos_jolla_nimi_ja_maara(self):
        t = Tuote("piimä", 5)
        self.kori.lisaa_tuote(t)
        self.kori.lisaa_tuote(t)
        
        self.assertEqual(len(self.kori.ostokset()), 1)
        self.assertEqual(self.kori.ostokset()[0].lukumaara(), 2)
        self.assertEqual(self.kori.ostokset()[0].tuotteen_nimi(), "piimä")


 
    def test_korissa_2_tuotetta_ja_yksi_poistetaan(self):
        t = Tuote("piimä", 5)
        self.kori.lisaa_tuote(t)
        self.kori.lisaa_tuote(t)
        self.kori.poista_tuote(t)

        self.assertEqual(len(self.kori.ostokset()), 1)
        self.assertEqual(self.kori.ostokset()[0].lukumaara(), 1)
        self.assertEqual(self.kori.ostokset()[0].tuotteen_nimi(), "piimä")





    
    def test_korin_tyhjennys(self):
        t = Tuote("juusto", 4)
        for i in range(5):
            self.kori.lisaa_tuote(t)

        self.kori.tyhjenna()
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
