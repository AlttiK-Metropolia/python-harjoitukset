class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, kuljettu_matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettu_matka = kuljettu_matka

auto = Auto("ABC-123", 143)
print(auto.rekisteritunnus)
print(auto.huippunopeus)
print(auto.nopeus)
print(auto.kuljettu_matka)