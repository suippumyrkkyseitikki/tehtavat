class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka

    def kiihdyta(self, muutos):
        self.nopeus += muutos

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit=0):
        self.matka += self.nopeus * tunnit

auto1 = Auto("ABC-123", 142, 60, 2000)

print(f"Auton rekisteritunnus on {auto1.rekisteritunnus}, "
      f"sen huippunopeus on {auto1.huippunopeus}km/h, "
      f"se on kulkenut {auto1.matka}km ja sen nopeus tällä hetkellä on {auto1.nopeus}km/h")

auto1.kulje(1.5)

print(f"Auton kuljettu matka on {auto1.matka}km")

