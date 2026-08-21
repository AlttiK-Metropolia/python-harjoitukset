leiviska = input("Anna leiviskien määrä: ")
naulat = input("Anna naulojen määrä: ")
luodit = input("Anna luotien määrä: ")

leiviska_paino = float(leiviska) * 20 * 32 * 13.3
naulat_paino = float(naulat) * 32 * 13.3
luodit_paino = float(luodit) * 13.3

print("Massa nykymittojen mukaan: \n" + str(int((leiviska_paino + naulat_paino + luodit_paino) / 1000)) + " kilogrammaa " + str(int((leiviska_paino + naulat_paino + luodit_paino) % 1000)) + " grammaa")