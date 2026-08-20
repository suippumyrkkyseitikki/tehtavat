s = input("Biologinen sukupuolesi?: ")
h = int(input("Hemoglobiiniarvo?: "))

if s == "nainen":
    if h < 117 :
        print("Hemoglobiiniarvosi on matala")
    if h > 177 :
        print("Hemoglobiiniarvosi on korkea")
    if h < 175 and h > 117 :
        print("Hemoglobiiniarvosi on normaali")

if s == "mies":
    if h < 134 :
        print("Hemoglobiiniarvosi on matala")
    if h > 195 :
        print("Hemoglobiiniarvosi on korkea")
    if h > 134 and h < 195 :
        print("Hemoglobiiniarvosi on normaali")