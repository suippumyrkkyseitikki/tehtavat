
def gallonatlitroiksi(gallonat):
    return gallonat * 3.785

gallona = 1
while gallona > 0:
    gallona = int(input("Montako gallonaa?: "))
    litrat = gallonatlitroiksi(gallona)
    print(litrat)