#Kysytään kanta ja korkeus
kanta = float(input("Suorakulmion kanta: "))
korkeus = float(input("Suorakulmion korkeus: "))

#Lasketaan
A = kanta * korkeus
P = kanta * 2 + korkeus * 2

#Tulostetaaan
print(f"Suorakulmion pinta-ala on {A} ja piiri {P}")