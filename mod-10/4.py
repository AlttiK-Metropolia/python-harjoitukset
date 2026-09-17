class Kilpailu:
    def __init__(self, nimi, pituus, kilpailijat=[]):
        self.nimi = nimi
        self.pituus = pituus
        self.kilpailijat = kilpailijat

    def tunti_kuluu(self):
        for kilpailija in self.kilpailijat:
            kilpailija.kulje(1)

    def tulosta_tilanne(self):
        for kilpailija in self.kilpailijat:
            print(f"Rekisteritunnus: {kilpailija.rekisteritunnus}")
            print(f"Huippunopeus: {kilpailija.huippunopeus}")
            print(f"Loppu nopeus: {kilpailija.nopeus}")
            print(f"Kuljettu matka: {kilpailija.kuljettu_matka}")
            print("\n")

    def kilpailu_ohi(self):
        for kilpailija in self.kilpailijat:
            if kilpailija.kuljettu_matka >= self.pituus:
                return kilpailija
        return False

import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, kuljettu_matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettu_matka = kuljettu_matka
    def kiihdyta(self, lisays):
        self.nopeus += lisays
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0
    def kulje(self, tunnit):
        self.kuljettu_matka += self.nopeus * tunnit

autot = []

for auto_nro in range(10):
    auto = Auto(f"ABC-{auto_nro + 1}", random.randint(100, 200))
    autot.append(auto)

kisa = Kilpailu("Suuri romuralli", 8000, autot)

while not kisa.kilpailu_ohi():
    for auto in autot:
        auto.kiihdyta(random.randint(-10, 15))
    kisa.tunti_kuluu()
    voittaja = kisa.kilpailu_ohi()
    if voittaja != False:
        print(f"Voittaja: {voittaja.rekisteritunnus}")
        print("\n")
        kisa.tulosta_tilanne()
        break