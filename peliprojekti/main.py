from luokat.pelaaja import Pelaaja
from luokat.roskakorit import Roskakori
from data import arvo_esineet, sijainnit
from random import randint
from vihollinen import rotta_tappelu
import os
TALLENNUS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "save.txt")
import time

paivan_pituus = 15 * 60

def aikaa_jäljellä(päivän_alku):
    return max(0, paivan_pituus - (time.time() - päivän_alku))

def muotoile_aika(sekunnit):
    minuutit, sekunnit = divmod(int(sekunnit), 60)
    return f"{minuutit:02d}:{sekunnit:02d}"

def save_pelaaja(pelaaja):
    with open(TALLENNUS, "w") as f:
        f.write(f"{pelaaja.raha:.2f},{pelaaja.elämät},{pelaaja.sijainti},{pelaaja.esineet['tila']},{nimi},{ikä}\n")
        f.write(",".join(pelaaja.esineet["esineet"]) + "\n")

def load_pelaaja():
    with open(TALLENNUS, "r") as f:
        data = f.readline().strip().split(",")
        raha, elämät, sijainti, tila, nimi, ikä = data
        pelaaja = Pelaaja(float(raha), int(elämät), sijainti)
        pelaaja.esineet["tila"] = int(tila)
        esineet = f.readline().strip().split(",")
        if len(esineet) > 0 and esineet[0] != "":
            pelaaja.esineet["esineet"] = esineet
        else:
            pelaaja.esineet["esineet"] = []
        return pelaaja, nimi, ikä

def nayta_paavalikko(sijainti):
    eka_valinta = "1. Etsi roskakoreja"
    if sijainti.lower() == "kauppa":
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
            if pelaaja.lisaa_esine(esine):
                print(f"- {esine} (tila: {tiedot['tila']}, arvo: {tiedot['arvo']:.2f} €)")
            else:
                print(f"- {esine} ei mahtunut reppuun (tarvitsee {tiedot['tila']} tilaa, vapaana {pelaaja.esineet['tila']})")

def palauta_pulloja(pelaaja):
    palautus = 0
    for esine in pelaaja.esineet["esineet"][:]: # kopioidaan lista jotta voidaan muokata alkuperäistä
        if esine in ["pullo_pieni", "pullo_iso", "tölkki"]:
            tiedot = arvo_esineet[esine]
            palautus += tiedot["arvo"]
            pelaaja.poista_esine(esine)

    pelaaja.lisaa_raha(palautus)
    return palautus

try:
    pelaaja, nimi, ikä = load_pelaaja()
    jatka = input(f"Löytyi tallennus pelaajalle {nimi}. Jatketaanko? (k/e): ").lower() == "k"
except (FileNotFoundError, ValueError):
    jatka = False

if jatka:
    print(f"Tervetuloa takaisin, {nimi}!")
else:
    nimi = input("Anna nimesi: ")
    ikä = int(input("Anna ikäsi: "))
    if ikä < 18:
        print("Et ole tarpeeksi vanha pelaamaan.")
        exit()
    pelaaja = Pelaaja(raha=0)

päivän_alku = time.time()
while True:
    print(f"\n⏰ Aikaa jäljellä: {muotoile_aika(aikaa_jäljellä(päivän_alku))}")
    nayta_paavalikko(pelaaja.sijainti)
    valinta = input("Valitse toiminto (1-4): ")

    if not valinta.isdigit() or not (1 <= int(valinta) <= 4):
        print("Virheellinen valinta.")
        continue

    if valinta == "1":
        if pelaaja.sijainti.lower() == "kauppa":
            palautus = palauta_pulloja(pelaaja)

            print(f"Palautit pulloja ja tölkkejä ja sait {palautus:.2f} €.")
        else:
            roskakori = valitse_roskakori(pelaaja)
            etsi_roskakori(pelaaja, roskakori)
    elif valinta == "2":
        uusi_sijainti = valitse_sijainti()
        pelaaja.siirry(uusi_sijainti)
    elif valinta == "3":
        pelaaja.tulosta_tiedot()
    elif valinta == "4":
        save_pelaaja(pelaaja)
        print("Kiitos pelaamisesta!")
        break
    else:
        print("Virheellinen valinta. Yritä uudelleen.")

    if pelaaja.raha >= 50:
        print(f"\n🎉 Sait kasaan {pelaaja.raha:.2f} € — voitit päivän!")
        break
    if aikaa_jäljellä(päivän_alku) <= 0:
        print(f"\n🌙 Päivä päättyi! Keräsit {pelaaja.raha:.2f} € / 50 €. Hävisit.")
        break
    if pelaaja.elämät <= 0:
        print("Kuolit. Peli päättyi!")
        break