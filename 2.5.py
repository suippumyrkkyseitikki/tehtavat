leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))


lpaino = luodit * 13.3

naula = 13.3 * 32

leiviska = naula * 20

lepaino = leiviska * leiviskat
npaino = naula * naulat

massa = npaino + lepaino + lpaino

kg = massa / 1000
gra = int(kg)

print("Massa nykymittojen mukaan: ")
print(f"{kg:.0f}kg ja {gra}g")



