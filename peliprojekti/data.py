arvo_esineet = {
    "tölkki": { "tila": 1, "arvo": 0.15 },
    "pullo_pieni": { "tila": 1, "arvo": 0.2 },
    "pullo_iso": { "tila": 2, "arvo": 0.4 },
    "näppäimistö": { "tila": 7, "arvo": 5 },
    "puhelin": { "tila": 5, "arvo": 10 },
    "tietokone": { "tila": 12, "arvo": 30 },
    "kello": { "tila": 3, "arvo": 15 },
    "kulta": { "tila": 5, "arvo": 45 },
    "sormus": { "tila": 3, "arvo": 40 },
}
vihut = {
    "rotta": { "tila": 1, "arvo": -1 },
    "piikki": { "tila": 1, "arvo": -2 },
}
## Pelaaja voi valita 3:sta eri alueesta. Puisto (enemmän pulloja, mutta enemmän piikkejä), Keskusta (enemmän arvoesineitä, mutta enemmän rottia), Asuinalue (pieni riski, mutta vain vähän pulloja, ruokaa ja arvoesineitä)
sijainnit = {
    "puisto": { "rotta": 0.4, "piikki": 0.8, "tölkki": 0.95, "pullo_pieni": 0.9, "pullo_iso": 0.8, "näppäimistö": 0.1, "puhelin": 0.1, "tietokone": 0.01, "kello": 0.01, "kulta": 0.001, "sormus": 0.0001 },
    "keskusta": { "rotta": 0.7, "piikki": 0.65, "tölkki": 0.8, "pullo_pieni": 0.7, "pullo_iso": 0.6, "näppäimistö": 0.4, "puhelin": 0.3, "tietokone": 0.2, "kello": 0.1, "kulta": 0.1, "sormus": 0.05 },
    "asuinalue": { "rotta": 0.2, "piikki": 0.1, "tölkki": 0.6, "pullo_pieni": 0.7, "pullo_iso": 0.3, "näppäimistö": 0.2, "puhelin": 0.1, "tietokone": 0.05, "kello": 0.05, "kulta": 0.05, "sormus": 0.05 },
    "kauppa": {}
}