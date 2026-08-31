import random

arvat = int(input("Montako arpakuutiota?: "))

summa = 0

for i in range(arvat):
    summa += random.randint(1,6)

print(f"Silmälukujen summa on {summa}")


