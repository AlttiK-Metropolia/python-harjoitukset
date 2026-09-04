def galloonalitraan(galloonat):
    return galloonat * 3.785

while True:
    galloona = int(input("Anna galloonat: "))
    if galloona < 0:
        break
    print(str(galloonalitraan(galloona)), "litraa")