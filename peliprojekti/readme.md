# Roskakori dyykkaus Simulaattori
### Altti Kolkki

## Pelin idea ja tarina

Pelaajalla on 50 euron pikavippi erääntymässä huomenna, eikä tilillä ole rahaa. Kaupunki on kuitenkin täynnä roskiksia, ja ihmiset heittävät pois kaikenlaista: pantillisia pulloja ja tölkkejä, vanhoja puhelimia, tietokoneita ja joskus jopa kultaa. Pelaaja lähtee dyykkaamaan ja yrittää kerätä rahat kokoon yhden päivän aikana.

## Tavoite

Kerää 50 euroa ennen kuin 15 minuutin päivä loppuu.

Peli päättyy:
- **voittoon**, kun pelaajalla on vähintään 50 euroa
- **tappioon**, jos päivä loppuu ennen sitä
- **tappioon**, jos pelaajan 10 sydäntä loppuvat

## Kestävä kehitys

- Kierrätys
- Uudelleenkäyttö

## Toimintaperiaatteet

1. Pelaaja valitsee alueen: puisto, keskusta tai asuinalue.
2. Alueella pelaaja etsii roskiksia ja valitsee niistä yhden tutkittavaksi.
3. Löydetyt esineet menevät reppuun, johon mahtuu 15 tilaa.
4. Roskiksessa voi olla rotta tai piikki. Jos pelaaja ei paina ENTER 1.5 sekunnissa, hän menettää 3 sydäntä.
5. Kun reppu täyttyy, pelaaja menee kauppaan ja myy tavarat rahaksi.
6. Tätä toistetaan, kunnes rahaa on 50 euroa, aika loppuu tai sydämet loppuvat.

Alueet eroavat toisistaan, joten jokainen niistä on oma reittinsä voittoon:
- Puisto: paljon pulloja, vähän arvoesineitä
- Keskusta: eniten arvoesineitä, mutta eniten vaaroja
- Asuinalue: turvallisin, kohtalaisesti tavaraa