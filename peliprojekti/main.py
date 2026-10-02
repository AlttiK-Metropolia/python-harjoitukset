from luokat.pelaaja import Pelaaja
from luokat.roskakorit import Roskakori
from data import arvo_esineet, sijainnit
from random import randint
from vihollinen import rotta_tappelu

def nayta_paavalikko(sijainti):
    eka_valinta = "1. Etsi roskakoreja"
    if sijainti == "Kauppa":
        eka_valinta = "1. Palauta pulloja"

    print(f"""
----------------------------------------------------
Sijainti: {sijainti}
Päävalikko:
{eka_valinta}
2. Vaihda sijaintia
3. Näytä tiedot
4. Lopeta
----------------------------------------------------""")

def valitse_sijainti():
    alueet = list(sijainnit.keys())
    print("\nMinne mennään?")
    for i, alue in enumerate(alueet, start=1):
        print(f"{i}. {alue}")

    while True:
        valinta = input("Valitse alue: ")
        if valinta.isdigit() and 1 <= int(valinta) <= len(alueet):
            return alueet[int(valinta) - 1]
        print("Virheellinen valinta.")


def valitse_roskakori(pelaaja):
    roskakorit = []
    for _ in range(randint(1, 3)):
        roskakori = Roskakori(pelaaja.sijainti)
        roskakorit.append(roskakori)

    for roskakori in roskakorit:
        roskakori.arvo_esineet()

    print("\nLöysit seuraavat roskakorit:")
    for i, roskakori in enumerate(roskakorit, start=1):
        print(f"{i}. Roskakori")

    while True:
        valinta = input(f"Valitse roskakori (1-{len(roskakorit)}): ")
        if valinta.isdigit() and 1 <= int(valinta) <= len(roskakorit):
            return roskakorit[int(valinta) - 1]
        print("Virheellinen valinta.")

def etsi_roskakori(pelaaja, roskakori):
    if pelaaja.esineet.get("tila", 0) <= 0:
        print("Inventaario on täynnä. Mene kauppaan palauttamaan esineitä.")
        return
    if not roskakori.esineet:
        print("Roskakori on tyhjä.")
        return

    print("Löysit seuraavat esineet:")
    for esine in roskakori.esineet:
        if esine == "rotta":
            rotta_tappelu(pelaaja)
        elif esine == "piikki":
            pelaaja.poista_elämä(2)
            print(f"Roskakorissa oli {esine}! Menetit kaksi elämää.")
        else:
            tiedot = arvo_esineet[esine]
            print(f"- {esine} (tila: {tiedot['tila']}, arvo: {tiedot['arvo']})")
            pelaaja.lisaa_esine(esine)

nimi = input("Anna nimesi: ")
ikä = input("Anna ikäsi: ")
if int(ikä) < 18:
    print("Et ole tarpeeksi vanha pelaamaan.")
    exit()

pelaaja = Pelaaja(raha=0)

while True:
    nayta_paavalikko(pelaaja.sijainti)
    valinta = input("Valitse toiminto (1-4): ")

    if not valinta.isdigit() or not (1 <= int(valinta) <= 4):
        print("Virheellinen valinta.")
        continue

    if valinta == "1":
        if pelaaja.sijainti == "Kauppa":
            print("\nPalautat pulloja ja saat rahaa!")
            palautus = pelaaja.esineet.get("pullot_pieni", 0) * arvo_esineet["pullo_pieni"]["arvo"]
            pelaaja.lisaa_raha(palautus)
        else:
            roskakori = valitse_roskakori(pelaaja)
            etsi_roskakori(pelaaja, roskakori)
    elif valinta == "2":
        uusi_sijainti = valitse_sijainti()
        pelaaja.siirry(uusi_sijainti)
    elif valinta == "3":
        pelaaja.tulosta_tiedot()
    elif valinta == "4":
        print("Kiitos pelaamisesta!")
        break
    else:
        print("Virheellinen valinta. Yritä uudelleen.")

    if pelaaja.raha >= 50:
        print(f"\n🎉 Sait kasaan {pelaaja.raha:.2f} € — voitit päivän!")
        break