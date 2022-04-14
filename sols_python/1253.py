entrada = int(input())
for c in range(entrada):
    texto = input()
    chave = int(input())
    textoDecodificado = ''
    for palavra in texto:
        if ord(palavra) - chave >= 65:
            textoDecodificado += chr(ord(palavra) - chave)
        else:
            posicao = 90 - (65 - (ord(palavra) - chave)) + 1
            textoDecodificado += chr(posicao)
    print(textoDecodificado)
