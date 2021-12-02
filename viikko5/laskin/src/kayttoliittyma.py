from enum import Enum
from tkinter import ttk, constants, StringVar


class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4

class Summa:
    def __init__(self, sovellus, lue):
        self.sovellus = sovellus
        self.lue = lue
        
    def suorita(self):
        self.arvo = self.lue()
        self.sovellus.plus(self.arvo)

    def kumoa(self):
        self.sovellus.miinus(self.arvo)
        

class Erotus:
    def __init__(self, sovellus, lue):
        self.sovellus = sovellus
        self.lue = lue

    def suorita(self):
        self.arvo = self.lue()
        self.sovellus.miinus(self.arvo)

    def kumoa(self):
        self.sovellus.plus(self.arvo)

class Nollaus:
    def __init__(self, sovellus):
        self.sovellus = sovellus

    def suorita(self):
        self.arvo = self.sovellus.tulos
        self.sovellus.nollaa()

    def kumoa(self):
        self.sovellus.aseta_arvo(self.arvo)


class Kumoa:
    def __init__(self, lue_komento):
        self.lue_komento = lue_komento

    def suorita(self):
        self.lue_komento().kumoa()

    def kumoa(self):
        pass

class Kayttoliittyma:
    def __init__(self, sovellus, root):
        self._sovellus = sovellus
        self._root = root
        self._viimeisin_komento = None

        self.__komennot = {
            Komento.SUMMA : Summa(self._sovellus, self._lue_syote),
            Komento.EROTUS : Erotus(self._sovellus, self._lue_syote),
            Komento.NOLLAUS : Nollaus(self._sovellus),
            Komento.KUMOA : Kumoa(self._lue_kumottava_komento)
        }

    def kaynnista(self):
        self._tulos_var = StringVar()
        self._tulos_var.set(self._sovellus.tulos)
        self._syote_kentta = ttk.Entry(master=self._root)

        tulos_teksti = ttk.Label(textvariable=self._tulos_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(Komento.SUMMA)
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS)
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.NOLLAUS)
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.KUMOA)
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)
        
    def _lue_syote(self):
        return int(self._syote_kentta.get())

    def _lue_kumottava_komento(self):
        return self._viimeisin_komento

    def _suorita_komento(self, komento):
        arvo = 0

        try:
            arvo = int(self._syote_kentta.get())
        except Exception:
            pass

        self.__komennot[komento].suorita()
        self._viimeisin_komento = self.__komennot[komento]

        if komento == Komento.KUMOA:
            self._kumoa_painike["state"] = constants.DISABLED
        else:
            self._kumoa_painike["state"] = constants.NORMAL

        if self._sovellus.tulos == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        self._syote_kentta.delete(0, constants.END)
        self._tulos_var.set(self._sovellus.tulos)
