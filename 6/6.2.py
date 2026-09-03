import random

def heita(tahkot):
     return random.randint(1, tahkot)

max = int(input("Anna nopan maksimisilmälukumäärä: "))

while True:
    silmaluku = heita(max)
    print(silmaluku)
    if silmaluku == max:
        break
