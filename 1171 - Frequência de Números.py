entrada = int(input())
lista = list()
for c in range(entrada):
    lista.append(int(input()))
for numero in range(1, 2001):
    if numero in lista:
        print(f'{numero} aparece {lista.count(numero)} vez(es)')
