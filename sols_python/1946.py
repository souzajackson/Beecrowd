from math import factorial
entrada = int(input()) - 1
possibilidadesTotais = 2 ** entrada
possibilidadesVencedoras = factorial(entrada) // factorial(int(entrada / 2)) ** 2
print(f'{(possibilidadesVencedoras / possibilidadesTotais) * 100:.2f}')
