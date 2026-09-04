import random

def noppa(tahkot):
    return random.randint(1, tahkot)

maksimi = int(input("Anna tahkojen määrä: "))

while True:
    numero = noppa(maksimi)
    print(numero)
    if numero == maksimi:
        break