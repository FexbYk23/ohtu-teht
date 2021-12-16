from kps import KPS
from tekoaly import Tekoaly


class KPSTekoaly(KPS):
    def __init__(self):
        self.aly = Tekoaly()

    def _toisen_siirto(self, ensimmaisen_siirto):
        return self.aly.anna_siirto()
