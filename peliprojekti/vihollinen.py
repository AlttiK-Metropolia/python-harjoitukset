import time

"""
Kuva saatu:
https://asciiart.website/art/7323
"""
ROTTA = r"""
 ,,==.                 __
((   ))    ,--~~~~-._ ( \\__
 `) ((._,-~   \      `'  '* `=#
     `---~\( _/,___( /_/`---~'
           ``==-    `=-
------------------------------------------------
"""
"""
Kuva saatu:
https://ascii.co.uk/art/syringe
"""
PIIKKI = r"""
                                       |
                 ,------------=--------|___________|
-=============%%%|         |  |______|_|___________|
                 | | | | | | ||| | | | |___________|
                 `------------=--------|           |
                                       |
"""

reaktioaika = 1.5

def vaara(pelaaja, kuva, nimi, vahinko):
    print(kuva)
    print(f"{nimi}! Paina ENTER {reaktioaika:.1f} sekunnissa!")

    alku = time.time()
    input()
    kesto = time.time() - alku

    if kesto <= reaktioaika:
        print(f"Väistit ajoissa! ({kesto:.2f} s)")
        return True

    print(f"Liian hidas ({kesto:.2f} s)! Menetit {vahinko} sydäntä.")
    pelaaja.poista_elämä(vahinko)
    return False

def rotta_tappelu(pelaaja):
    return vaara(pelaaja, ROTTA, "Rotta", 2)

def piikki_vaara(pelaaja):
    return vaara(pelaaja, PIIKKI, "Käytetty piikki", 2)