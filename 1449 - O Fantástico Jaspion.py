entrada = int(input())
for c in range(entrada):
    dicionario = dict()
    entrada = input().split()
    entrada[0] = int(entrada[0])
    entrada[1] = int(entrada[1])
    for c in range(entrada[0]):
        palavraJapones = input()
        palavraPortugues = input()
        dicionario[palavraJapones] = palavraPortugues
    for c in range(entrada[1]):
        frase = input().split()
        fraseDecodificada = ''
        for palavra in frase:
            if palavra in dicionario:
                fraseDecodificada += dicionario[palavra]
                fraseDecodificada += ' '
            else:
                fraseDecodificada += palavra
                fraseDecodificada += ' '
        print(fraseDecodificada[:-1])
    print()
