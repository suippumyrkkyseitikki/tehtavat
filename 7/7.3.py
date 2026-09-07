lentoasemat = {}

while True:
    print("1 - Syötä uusi lentoasema")
    print("2 - Hae lentoasema")
    print("3 - Lopeta")

    toiminto = input("Valinta: ")

    if toiminto == "1":
        icao = input("ICAO-koodi: ")
        nimi = input("Lentoaseman nimi: ")
        lentoasemat[icao] = nimi

    elif toiminto == "2":
        icao = input("ICAO-koodi: ")
        if icao in lentoasemat:
            print(lentoasemat[icao])
        else:
            print("Lentoasemaa ei löydy.")

    elif toiminto == "3":
        break

    else:
        print("Virheellinen valinta")