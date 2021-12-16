from kps import KPS
from tekoaly_parannettu import TekoalyParannettu


class KPSParempiTekoaly(KPS):
    def __init__(self):
        self.aly = TekoalyParannettu(10)

    def _toisen_siirto(self, ensimmaisen_siirto):
        siirto = self.aly.anna_siirto()
        self.aly.aseta_siirto(ensimmaisen_siirto)
        return siirto
