luvut = []

numero = (input("Syötä numero: "))
while numero!= "":
    luvut.append(int(numero))
    numero = (input("Syötä seuraava numero: "))

suurimmat = sorted(luvut, reverse=True)[:5]
print(suurimmat)