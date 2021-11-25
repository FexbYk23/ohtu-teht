from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        self.__ostokset = []

    def __etsi_ostos(self, etsittava : Tuote):
        for ostos in self.__ostokset:
            if ostos.tuote == etsittava:
                return ostos
        return None

    def tavaroita_korissa(self):
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 
        return sum(map(lambda ostos : ostos.lukumaara(), self.__ostokset))

# kertoo korissa olevien ostosten yhteenlasketun hinnan
    def hinta(self):
        return sum(map(lambda ostos : ostos.hinta(), self.__ostokset))


    def lisaa_tuote(self, lisattava: Tuote):
        ostos = self.__etsi_ostos(lisattava)
        if ostos == None:
            # lisää tuotteen
            self.__ostokset.append(Ostos(lisattava))
        else:
            ostos.muuta_lukumaaraa(1)

    def poista_tuote(self, poistettava: Tuote):
        ostos = self.__etsi_ostos(poistettava)
        if ostos != None:
            self.__ostokset.remove(ostos)


    def tyhjenna(self):
        self.__ostokset = []

    def ostokset(self):
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
        return self.__ostokset
