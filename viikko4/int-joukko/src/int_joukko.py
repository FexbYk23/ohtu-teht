KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        self.kapasiteetti = self.__validoi_numero(kapasiteetti, "Väärä kapasiteetti")
        self.kasvatuskoko = self.__validoi_numero(kasvatuskoko, "Väärä kasvatuskoko")
        self.luvut = [0] * self.kapasiteetti
        self.koko = 0

    @staticmethod
    def __validoi_numero(numero, virhe_viesti):
        if not isinstance(numero, int) or numero < 0:
            raise Exception(virhe_viesti)
        else:
            return numero

    def kuuluu(self, luku):
        return luku in self.luvut[0:self.koko]

    def lisaa(self, luku):
        if self.kuuluu(luku):
            return False
        
        self.luvut[self.koko] = luku
        self.koko = self.koko + 1

        if self.koko == len(self.luvut):
            self.luvut.extend([0] * self.kasvatuskoko)
        return True

    def poista(self, luku):
        for i in range(0, self.koko):
            if luku == self.luvut[i]:
                self.luvut[i] = self.luvut[self.koko - 1]
                self.koko = self.koko - 1
                return True
        return False

    def mahtavuus(self):
        return self.koko

    def to_int_list(self):
        return [self.luvut[i] for i in range(self.koko)]

    @staticmethod
    def yhdiste(a, b):
        yhdiste = IntJoukko()
        yhdiste.lisaaJoukko(a)
        yhdiste.lisaaJoukko(b)
        return yhdiste

    @staticmethod
    def leikkaus(a, b):
        leikkaus = IntJoukko()
        
        for i in range(0, a.koko):
            for j in range(0, b.koko):
                if a.luvut[i] == b.luvut[j]:
                    leikkaus.lisaa(b.luvut[j])

        return leikkaus

    @staticmethod
    def erotus(a, b):
        erotus = IntJoukko()
        erotus.lisaaJoukko(a)

        for i in range(0, b.koko):
            erotus.poista(b.luvut[i])

        return erotus
    
    def lisaaJoukko(self, joukko):
        for alkio in joukko.luvut[0:joukko.koko]:
            self.lisaa(alkio)

    def __str__(self):
        jono_str = str(self.luvut[0:self.koko])
        return "{" + jono_str[1:-1] + "}"

