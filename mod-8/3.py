lentoasemat = {}
while True:
    valinta = input("Haluatko tehdä uuden haun, syöttää uuden, vai lopettaa? (haku/uusi/lopeta): ").lower()
    if valinta == "haku":
        ICAO = input("Anna lentoaseman ICAO-koodi: ")
        if ICAO in lentoasemat:
            print(f"Lentoasema: {lentoasemat[ICAO]}")
        else:
            print("Lentoasemaa ei löytynyt.")
    elif valinta == "uusi":
        ICAO = input("Anna lentoaseman ICAO-koodi: ")
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[ICAO] = nimi
    else:
        print("Ohjelma lopetetaan.")