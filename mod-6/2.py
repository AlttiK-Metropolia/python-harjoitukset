annetut_numerot = []
while True:
    numero = input("Anna numero: ")
    if numero == "":
        break
    annetut_numerot.append(int(numero))

annetut_numerot.sort(reverse=True)
for numero in annetut_numerot[0:5]:
    print(numero)