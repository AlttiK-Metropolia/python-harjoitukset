sukupuoli = input("Anna sukupuoli (m/n): ").lower()
hemogolobiini = float(input("Anna hemoglobiiniarvo (g/l): "))
if sukupuoli == "m":
    if hemogolobiini < 134:
        print("Hemoglobiiniarvo on alhainen")
    elif hemogolobiini > 195:
        print("Hemoglobiiniarvo on korkea")
    else:
        print("Hemoglobiiniarvo on normaali")
if sukupuoli == "n":
    if hemogolobiini < 117:
        print("Hemoglobiiniarvo on alhainen")
    elif hemogolobiini > 175:
        print("Hemoglobiiniarvo on korkea")
    else:
        print("Hemoglobiiniarvo on normaali")