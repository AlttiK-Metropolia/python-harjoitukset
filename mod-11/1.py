class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, sivumäärä, kirjoittaja, nimi):
        self.sivumäärä = sivumäärä
        self.kirjoittaja = kirjoittaja
        super().__init__(nimi)
    def tulosta_tiedot(self):
        print(f"Kirja: {self.nimi}, kirjoittaja: {self.kirjoittaja}, sivumäärä: {self.sivumäärä}")

class Lehti(Julkaisu):
    def __init__(self, päätoimittaja, nimi):
        self.päätoimittaja = päätoimittaja
        super().__init__(nimi)
    def tulosta_tiedot(self):
        print(f"Lehti: {self.nimi}, päätoimittaja: {self.päätoimittaja}")

lehti = Lehti("Aki Hyyppä", "Aku Ankka")
kirja = Kirja(200, "Rosa Liksom", "Hytti n:o 6")

lehti.tulosta_tiedot()
kirja.tulosta_tiedot()