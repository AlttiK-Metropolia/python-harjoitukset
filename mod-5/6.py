import random

numero = int(input("Anna arvottavien pisteiden määrä: "))

n = 0
i = 0

while i < numero:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x ** 2 + y ** 2 < 1:
        n += 1
    i += 1

pii = 4 * n / numero
print("Piin likiarvo on", pii)