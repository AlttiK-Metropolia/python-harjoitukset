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

reaktioaika = 1.5

def rotta_tappelu(pelaaja):
    print(ROTTA)
    print(f"Rotta! Paina ENTER {reaktioaika:.1f} sekunnissa!")

    alku = time.time()
    input()
    kesto = time.time() - alku

    if kesto <= reaktioaika:
        print(f"Väistit rotan ajoissa! ({kesto:.2f} s)")
        return True

    print(f"Liian hidas ({kesto:.2f} s)! Rotta puri, menetit 2 sydäntä.")
    pelaaja.poista_elämä(2)
    return False