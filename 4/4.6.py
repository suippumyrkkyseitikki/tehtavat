import random

N = 100000
n = 0
i = 0

while i < N:
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if x**2 + y**2 < 1:
        n += 1
    i += 1

pii = 4*n/N
print(pii)