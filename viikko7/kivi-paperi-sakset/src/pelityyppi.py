from kps import KPS
from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

class Pelityyppi:
    def __init__(self, kuvaus, peli):
        self.kuvaus = kuvaus
        self.peli = peli
    
    def pelaa(self):
        print("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s")
        self.peli.pelaa()

    def pelaaja_vs_pelaaja():
        return Pelityyppi("Ihmistä vastaan", KPSPelaajaVsPelaaja())
    
    def tekoaly():
        return Pelityyppi("Tekoälyä vastaan", KPSTekoaly())

    def parempi_tekoaly():
        return Pelityyppi("Parannettua tekoalyä vastaan", KPSParempiTekoaly())
    
    def __str__(self):
        return self.kuvaus


