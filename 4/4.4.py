import random

arpa = random.randint(1,10)

while True:
    arvaa = int(input("Arvaa numero: "))
    if arvaa < arpa:
        print("Liian pieni arvaus")
    elif arvaa > arpa:
        print("Liian suuri arvaus")
    if arpa == arvaa:
        print("Oikein")
        break