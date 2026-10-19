class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = matka
        self.matka = matka

    def kiihdyta(self, muutos):
        self.nopeus += muutos

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

auto1 = Auto("ABC-123", 142)

print(f"Auton rekisteritunnus on {auto1.rekisteritunnus}, "
      f"sen huippunopeus on {auto1.huippunopeus}km/h, "
      f"se on kulkenut {auto1.matka}km ja sen nopeus tällä hetkellä on {auto1.nopeus}km/h")

auto1.kiihdyta(30)
auto1.kiihdyta(70)
auto1.kiihdyta(50)

print(f"Auton nopeus kiihdytysten jälkeen on {auto1.nopeus}km/h")

auto1.kiihdyta(-200)

print(f"Auton nopeus hätäjarrutuksen jälkeen on {auto1.nopeus}km/h")
