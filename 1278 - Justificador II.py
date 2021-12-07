outputs = 0
while True:
    entrada = int(input())
    if entrada == 0:
        break
    if outputs != 0:
        print()
    frases = list()
    for c in range(entrada):
        frase = input().split()
        frase = ' '.join(frase)
        frases.append(frase)
    maiorFrase = 0
    for frase in frases:
        if len(frase) > maiorFrase:
            maiorFrase = len(frase)
    for frase in frases:
        print(' ' * (maiorFrase - len(frase)) + frase)
    outputs += 1