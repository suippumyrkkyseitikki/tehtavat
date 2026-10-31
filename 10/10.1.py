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


hissih = Hissi(9, 1)

hissih.siirry_kerrokseen(5)