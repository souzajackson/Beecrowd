entrada1 = int(input())
strings = list()
for c in range(entrada1):
    entrada = input()
    strings.append(entrada)
for frase in strings:
    fraseEmArray = frase.split()
    if len(fraseEmArray[0]) <= len(fraseEmArray[1]):
        menorPalavra = len(fraseEmArray[0])
    else:
        menorPalavra = len(fraseEmArray[1])
    palavra = ''
    for c in range(menorPalavra):
        palavra += fraseEmArray[0][c]
        palavra += fraseEmArray[1][c]
    if len(fraseEmArray[0]) > menorPalavra:
        for c in range(menorPalavra, len(fraseEmArray[0])):
            palavra += fraseEmArray[0][c]
    elif len(fraseEmArray[1]) > menorPalavra:
        for c in range(menorPalavra, len(fraseEmArray[1])):
            palavra += fraseEmArray[1][c]
    print(palavra)
    