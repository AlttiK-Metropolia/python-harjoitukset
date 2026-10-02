import random
from data import arvo_esineet, sijainnit

class Roskakori:
    MAX_ESINEET = 7 
    MAX_TILA = 15

    def __init__(self, sijainti):
        self.esineet = []
        self.sijainti = sijainti

    def arvo_esineet(self):
        ## Harvinaisuus, ja pelaajan sijainti määrittää todennäköisyyden, että esine arvotaan roskakoriin.
        ## Esineitä voi olla useampi kappale, mutta roskakoriin mahtuu enintään 7 esinettä, tai 15 "tilaa".
        todennakoisyydet = sijainnit[self.sijainti]
        kaytetty_tila = 0

        for esine, tiedot in arvo_esineet.items():
            todnak = todennakoisyydet.get(esine)

            yritykset = 1
            if todnak > 0.5:
                yritykset = random.randint(3, 5)

            for _ in range(yritykset):
                # Onko roskakori jo täynnä?
                if len(self.esineet) >= self.MAX_ESINEET:
                    return
                # Osuiko arpa tälle esineelle?
                if random.random() >= todnak:
                    continue
                # Mahtuuko se vielä tilan puolesta?
                if kaytetty_tila + tiedot["tila"] > self.MAX_TILA:
                    continue

                self.esineet.append(esine)
                kaytetty_tila += tiedot["tila"]
            if random.random() < sijainnit[self.sijainti]["rotta"]:
                self.esineet.append("rotta")