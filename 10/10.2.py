class Talo:
    def __init__(self, ylin, alin, lkm):
        self.hissit = []
        for i in range(lkm):
            hissit.append(Hissi(alin, ylin))

    def aja_hissiä(self,hissi_numero,mihin):
        hissi_numero = len(hissit)






class Hissi:
    def __init__(self, ylin, alin):
        self.ylin = ylin
        self.alin = alin
        self.kerros = alin

    def siirry_kerrokseen(self, mihin):
        while self.kerros < mihin:
            self.kerros_ylös()

        while self.kerros > mihin:
            self.kerros_alas()


    def kerros_ylös(self):
        if self.kerros < self.ylin:
            self.kerros += 1
            print(f"hissi on nyt kerroksessa {self.kerros}")


    def kerros_alas(self):
        if self.kerros > self.alin:
            self.kerros -= 1
            print(f"hissi on nyt kerroksessa {self.kerros}")

talo1 = Talo(10, 1, 3)


