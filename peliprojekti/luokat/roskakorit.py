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

        # Sekoitetaan järjestys, etteivät pullot täytä roskista aina ennen arvoesineitä
        esineet = list(arvo_esineet.items())
        random.shuffle(esineet)

        for esine, tiedot in esineet:
            todnak = todennakoisyydet.get(esine, 0)

            yritykset = 1
            if todnak > 0.5:
                yritykset = random.randint(1, 3)

            for _ in range(yritykset):
                if len(self.esineet) >= self.MAX_ESINEET:
                    break
                if random.random() >= todnak:
                    continue
                if kaytetty_tila + tiedot["tila"] > self.MAX_TILA:
                    continue

                self.esineet.append(esine)
                kaytetty_tila += tiedot["tila"]

        # Vihut arvotaan erikseen, eivätkä ne vie roskiksen tilaa
        for vihu in ("rotta", "piikki"):
            if random.random() < todennakoisyydet.get(vihu, 0):
                self.esineet.append(vihu)
                break