def listasumma(lista):
    summa = 0
    for numero in lista:
        summa += numero
    return summa

test_lista1 = [1, 4, 7, 2]
test_lista2 = [2, 3]
test_lista3 = [2, 3, 7]
print(listasumma(test_lista1))
print(listasumma(test_lista2))
print(listasumma(test_lista3))