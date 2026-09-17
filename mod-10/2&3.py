class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros = alin_kerros
    def siirry_kerrokseen(self, kerros):
        for i in range(kerros + self.ylin_kerros):
            if self.kerros < kerros:
                self.kerros_ylos()
            elif self.kerros > kerros:
                self.kerros_alas()
    def kerros_ylos(self):
        if self.kerros < self.ylin_kerros:
            self.kerros += 1
            print(f"Hissi on kerroksessa {self.kerros}")
    def kerros_alas(self):
        if self.kerros > self.alin_kerros:
            self.kerros -= 1
            print(f"Hissi on kerroksessa {self.kerros}")

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissi_maara):
        self.hissit = []
        for i in range(hissi_maara):
            self.hissit.append(Hissi(alin_kerros, ylin_kerros))
    def aja_hissi(self, hissi_nro, kerros):
        self.hissit[hissi_nro].siirry_kerrokseen(kerros)
    def palohälytys(self):
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(hissi.alin_kerros)

talo = Talo(1, 5, 4)
talo.aja_hissi(0, 5)
talo.aja_hissi(1, 3)
talo.aja_hissi(0, 2)
talo.palohälytys()