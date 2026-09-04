vuodenajat = {
    "talvi": [12, 1, 2],
    "kevät": [3, 4, 5],
    "kesä": [6, 7, 8],
    "syksy": [9, 10, 11]
}

kuukausinumero = int(input("Anna kuukauden numero: "))
for vuodenaika, kuukaudet in vuodenajat.items():
    if kuukausinumero in kuukaudet:
        print(vuodenaika)
        break
else:
    print("Annettu kuukausi ei kuulu mihinkään vuodenaikaa")