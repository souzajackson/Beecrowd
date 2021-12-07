entrada1 = int(input())
valores = list()
pares = list()
impares = list()
for c in range(entrada1):
    entrada = int(input())
    valores.append(entrada)
for elemento in valores:
    if elemento % 2 == 0:
        pares.append(elemento)
    else:
        impares.append(elemento)
pares.sort()
impares.sort(reverse = True)
for numero in pares:
    print(numero)
for numero in impares:
    print(numero)