from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        self.ostokset = []

    def __etsi_ostos(self, etsittava : Tuote):
        for ostos in self.ostokset:
            if ostos.tuote == etsittava:
                return ostos
        return None

    def tavaroita_korissa(self):
        pass
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 


# kertoo korissa olevien ostosten yhteenlasketun hinnan
    def hinta(self):
        summa = 0
        for ostos in self.ostokset:
            summa += ostos.hinta()
        return summa 

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        self.ostokset.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        ostos = self.__etsi_ostos(poistettava)
        if ostos != None:
            self.ostokset.remove(ostos)


    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        pass
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
