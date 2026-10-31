class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f"Nimi: {self.nimi}")



class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kirjan kirjailija on {self.kirjoittaja}, ja kirjassa on {self.sivumaara} sivua")



class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        self.paatoimittaja = paatoimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Lehden päätoimittaja: {self.paatoimittaja}")



AkuAnkka = Lehti("Aku Ankka", "Aki Hyyppä" )
Hytti = Kirja("Hytti nro 6", "Rosa Liksom", 200)

Hytti.tulosta_tiedot()
AkuAnkka.tulosta_tiedot()


