import random


def heita():
     return random.randint(1, 6)

while True:
    silmaluku = heita()
    print(silmaluku)
    if silmaluku == 6:
        break



