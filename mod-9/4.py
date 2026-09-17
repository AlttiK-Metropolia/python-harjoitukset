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

kisa_akttivinen = True
while kisa_akttivinen:
    for auto in autot:
        auto.kiihdyta(random.randint(-10, 15))
        auto.kulje(1)
        if auto.kuljettu_matka >= 10000:
            kisa_akttivinen = False
            print(f"Voittaja: {auto.rekisteritunnus}")
            print("\n")
            for auto_ominaisuudet in autot:
                print(f"Rekisteritunnus: {auto_ominaisuudet.rekisteritunnus}")
                print(f"Huippunopeus: {auto_ominaisuudet.huippunopeus}")
                print(f"Loppu nopeus: {auto_ominaisuudet.nopeus}")
                print(f"Kuljettu matka: {auto_ominaisuudet.kuljettu_matka}")
                print("\n")
            break