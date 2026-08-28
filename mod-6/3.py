luku = int(input("Anna kokonaisluku: "))

alkuluku = True
jakaja = 2
while jakaja < luku:
    if luku % jakaja == 0:
        alkuluku = False
        break
    jakaja += 1

if alkuluku:
    print(luku, "on alkuluku")
else:
    print(luku, "ei ole alkuluku")