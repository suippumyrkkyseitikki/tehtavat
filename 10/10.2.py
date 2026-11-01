class Talo:
    def __init__(self, ylin, alin, lkm):
        self.hissit = []
        for i in range(lkm):
            self.hissit.append(Hissi(ylin, alin, i + 1))

    def aja_hissiä(self, hissi_numero, mihin):
        hissi = self.hissit[hissi_numero]
        hissi.siirry_kerrokseen(mihin)

class Hissi:
    def __init__(self, ylin, alin, numero):
        self.ylin = ylin
        self.alin = alin
        self.kerros = alin
        self.numero = numero

    def siirry_kerrokseen(self, mihin):
        while self.kerros < mihin:
            self.kerros_ylös()

        while self.kerros > mihin:
            self.kerros_alas()

    def kerros_ylös(self):
        if self.kerros < self.ylin:
            self.kerros += 1
            print(f"Hissi {self.numero}: kerros {self.kerros}")

    def kerros_alas(self):
        if self.kerros > self.alin:
            self.kerros -= 1
            print(f"Hissi {self.numero}: kerros {self.kerros}")


talo1 = Talo(10, 1, 3)

talo1.aja_hissiä(0, 5)
talo1.aja_hissiä(2, 8)


