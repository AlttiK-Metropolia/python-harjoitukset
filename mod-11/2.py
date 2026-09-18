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


class Sähköauto(Auto):
    def __init__(self, akkukapasiteetti, rekisteritunnus, huippunopeus):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, tankin_koko, rekisteritunnus, huippunopeus):
        super().__init__(rekisteritunnus, huippunopeus)
        self.tankin_koko = tankin_koko

sahkoauto = Sähköauto(52.5, "ABC-15", 180)
polttomoottoriauto = Polttomoottoriauto(32.3, "ABC-123", 165)

sahkoauto.kiihdyta(50)
sahkoauto.kulje(3)
polttomoottoriauto.kiihdyta(60)
polttomoottoriauto.kulje(3)
print(f"Sähköauton kuljettu matka: {sahkoauto.kuljettu_matka} km")
print(f"Polttomoottoriauton kuljettu matka: {polttomoottoriauto.kuljettu_matka} km")