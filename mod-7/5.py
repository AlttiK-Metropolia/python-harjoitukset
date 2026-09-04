def lista_parilliset(lista):
    parilliset = []
    for numero in lista:
        if numero % 2 == 0:
            parilliset.append(numero)

    return parilliset

testilista1 = [1, 2, 3, 4, 5, 6, 7]
print(f"Koko lista: {testilista1}")
print(f"Vain parilliset: {lista_parilliset(testilista1)}")