from math import sqrt

def isPrimo(n):
    if n % 2 == 0 and n != 2:
        return 'Not Prime'
    elif sqrt(n) == sqrt(n) // 1:
        return 'Not Prime'
    else:
        divisores = 0
        for c in range(3,int(sqrt(n) // 1 + 1), 2):
            if n % c == 0:
                divisores += 1
                break
        if divisores == 0:
            return 'Prime'
        else:
            return 'Not Prime'


entrada = int(input())
lista = list()
for c in range(entrada):
    entrada = int(input())
    lista.append(entrada)
for numero in lista:
    print(isPrimo(numero))
