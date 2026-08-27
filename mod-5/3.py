luvut = []
while True:
    luku = input("Anna luku: ")
    if luku == "":
        print("Pienin luku: " + str(min(luvut)) + ", suurin luku: " + str(max(luvut)))
        break
    luvut.append(int(luku))