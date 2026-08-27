yritykset = 0
while True:
    kayttajatunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")
    yritykset += 1
    if kayttajatunnus == "python" and salasana == "rules":
        print("Tervetuloa")
        break
    elif yritykset == 5:
        print("Pääsy evätty")
        break
    else:
        print("Pääsy evätty")