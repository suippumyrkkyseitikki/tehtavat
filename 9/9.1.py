class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka

auto1 = Auto("ABC-123", 142)

print(f"Auton rekisteritunnus on {auto1.rekisteritunnus}, "
      f"sen huippunopeus on {auto1.huippunopeus}km/h, "
      f"se on kulkenut {auto1.matka} km ja sen nopeus tällä hetkellä on {auto1.nopeus} km/h")