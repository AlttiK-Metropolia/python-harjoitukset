nimi = input("Anna nimesi: ")
ika = input("Anna ikäsi: ")

print("Nimi: " + nimi)
print("Ikä: " + ika)

paavalikko = """
----------------------------------------------------
Päävalikko:
1. Aloita peli
2. Asetukset
3. Lopeta
----------------------------------------------------
"""

if int(ika) < 12:
    print("Olet alaikäinen.")
elif ika == "Lopeta":
    print("Ohjelma lopetetaan.")
else:
    print("Tervetuloa!")
    print(paavalikko)
    while True:
        valinta = input("Valitse toiminto (1-3): ")
        if valinta == "1":
            print("Aloitetaan peli...")
        elif valinta == "2":
            print("Asetukset-valikko...")
        elif valinta == "3":
            print("Ohjelma lopetetaan.")
            break
        else:
            print("Virheellinen valinta. Yritä uudelleen.")

        print(paavalikko)
