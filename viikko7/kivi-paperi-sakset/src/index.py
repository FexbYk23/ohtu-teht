from pelityyppi import Pelityyppi

def main():
    pelityypit = {
            "a" : Pelityyppi.pelaaja_vs_pelaaja(),
            "b" : Pelityyppi.tekoaly(),
            "c" : Pelityyppi.parempi_tekoaly()
    }

    print("Valitse pelataanko")
    for vaihtoehto in pelityypit.keys():
        print(f"({vaihtoehto}) {pelityypit[vaihtoehto]}")
    print("\nMuilla valinnoilla lopetetaan")

    vastaus = input()
    if vastaus in pelityypit.keys():
        pelityypit[vastaus].pelaa()


if __name__ == "__main__":
    main()
