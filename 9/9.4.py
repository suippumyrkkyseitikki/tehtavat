
import random

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


autot = []

for i in range(1, 11):
    huippunopeus = random.randint(100, 200)
    rekisteritunnus = f"ABC-{i}"
    auto = Auto(rekisteritunnus, huippunopeus)
    autot.append(auto)


kilpailu_jatkuu = True

while kilpailu_jatkuu:
    for auto in autot:
        muutos = random.randint(-10, 15)
        auto.kiihdyta(muutos)
        auto.kulje(1)

    for auto in autot:
        if auto.matka >= 10000:
            kilpailu_jatkuu = False


for i in range(len(autot)):
    for j in range(i + 1, len(autot)):
        if autot[j].matka > autot[i].matka:
            autot[i], autot[j] = autot[j], autot[i]

print(f"{'Sija':<6}{'Rekisteritunnus':<18}{'Huippunopeus':>15}{'Nopeus':>12}{'Matka (km)':>15}")
print("-" * 66)

for sija, auto in enumerate(autot, start=1):
    print(f"{sija:<6}{auto.rekisteritunnus:<18}"
          f"{auto.huippunopeus:>15}"
          f"{auto.nopeus:>12}"
          f"{auto.matka:>15.1f}")