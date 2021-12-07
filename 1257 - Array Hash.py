entrada = int(input())
alfabeto = list()
for char in range(65, 91):
    alfabeto.append(chr(char))
for c in range(entrada):
    quantidadeDeCasos = int(input())
    tot = 0
    elemento = 0
    for c in range(quantidadeDeCasos):
        entrada = input()
        for pos, char in enumerate(entrada):
            tot += pos + elemento + alfabeto.index(char)
        elemento += 1
    print(tot)
