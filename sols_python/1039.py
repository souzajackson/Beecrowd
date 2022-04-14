from sys import stdin
from math import sqrt
for entrada in stdin:
    medidas = [int(n) for n in entrada.split()]
    cacador = medidas[:3]
    flor = medidas[3:]
    if cacador[0] >= sqrt((abs(flor[1] - cacador[1])) ** 2 + (abs(flor[2] - cacador[2])) ** 2) + flor[0]:
        print('RICO')
    else:
        print('MORTO')
