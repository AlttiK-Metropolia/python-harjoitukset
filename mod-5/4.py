from random import randint
arvattava_luku = randint(1, 10)

while True:
    arvaus = int(input("Arvaa luku väliltä 1-10: "))
    if arvaus < arvattava_luku:
        print("Liian pieni arvaus.")
    elif arvaus > arvattava_luku:
        print("Liian suuri arvaus.")
    else:
        print("Oikein")
        break