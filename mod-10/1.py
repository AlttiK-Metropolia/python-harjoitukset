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

hissi = Hissi(1, 5)
hissi.siirry_kerrokseen(5)
hissi.siirry_kerrokseen(1)