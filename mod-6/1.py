import random

arpakuutiot_lkm = int(input("Arpakuutioiden lukumäärä: "))
summa = 0
for arpakuutio in range(arpakuutiot_lkm):
    summa += random.randint(1, 6)

print("Summa: " + str(summa))