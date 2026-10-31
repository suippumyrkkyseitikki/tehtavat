class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka



    def aja(self, tunnit):
        self.matka += self.nopeus * tunnit


#sähköauto
class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(rekisteritunnus, huippunopeus,)


#polttomoottoriauto
class Polttomoottoriauto(Auto):
    def __init__(self,rekisteritunnus, huippunopeus, bensatankin_koko):
        self.bensatankin_koko = bensatankin_koko
        super().__init__(rekisteritunnus, huippunopeus)



sauto = Sähköauto("ABC-15", 180, 52.5)
pmauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sauto.nopeus = 100
pmauto.nopeus = 120

sauto.aja(3)
pmauto.aja(3)

print(f"Sähköauton matkamittari: {sauto.matka} km")
print(f"Polttomoottoriauton matkamittari: {pmauto.matka} km")