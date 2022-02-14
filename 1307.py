from math import gcd
quantidade_de_casos = int(input())

for c in range(quantidade_de_casos):
    lista = [int(input(), 2), int(input(), 2)]
    lista.sort()
    divisor = gcd(lista[0], lista[1])
    print(f'Pair #{c + 1}: All you need is love!' if divisor != 1 else f'Pair #{c + 1}: Love is not all you need!')
