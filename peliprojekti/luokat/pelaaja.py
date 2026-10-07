from data import arvo_esineet

class Inventaario:
    def __init__(self):
        self.esineet = {
            "tila": 15,
            "esineet": []
        }

    def lisaa_esine(self, esine):
        tiedot = arvo_esineet[esine]
        if self.esineet["tila"] - tiedot["tila"] >= 0:
            self.esineet["esineet"].append(esine)
            self.esineet["tila"] -= tiedot["tila"]

    def poista_esine(self, esine):
        tiedot = arvo_esineet[esine]
        if esine in self.esineet["esineet"]:
            self.esineet["esineet"].remove(esine)
            self.esineet["tila"] += tiedot["tila"]

class Sijainti:
    def __init__(self, sijainti="Kauppa"):
        self.sijainti = sijainti

    def siirry(self, uusi_sijainti):
        self.sijainti = uusi_sijainti

class Pelaaja(Inventaario, Sijainti):
    def __init__(self, raha, elämät=10, sijainti="Kauppa"):
        super().__init__()
        self.raha = raha
        self.elämät = elämät
        self.sijainti = sijainti

    def poista_elämä(self, maara):
        self.elämät -= maara

    def lisaa_elämä(self, maara):
        self.elämät += maara

    def lisaa_raha(self, maara):
        self.raha += maara

    def inventaarion_arvo(self):
        return sum(arvo_esineet[esine]["arvo"] for esine in self.esineet["esineet"])

    def tulosta_tiedot(self):
        esineet = self.esineet["esineet"]
        print(f"""Pelaajan tiedot:
        Raha: {self.raha:.2f} €
        Elämät: {self.elämät}
        Sijainti: {self.sijainti}
        Inventaario:
            Tila: {self.esineet['tila']}
            Esineet: {', '.join(esineet) if esineet else 'Ei esineitä'}
            Arvo: {self.inventaarion_arvo():.2f} €
""")