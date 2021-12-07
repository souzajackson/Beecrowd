entrada = int(input())
for c in range(entrada):
    texto = input().lower()
    maisFrequentes = list()
    contagemMaisFrequente = 0
    for char in range(97, 123):
        quantidadeDaLetra = texto.count(chr(char))
        if quantidadeDaLetra == contagemMaisFrequente:
            maisFrequentes.append(chr(char))
        elif quantidadeDaLetra > contagemMaisFrequente:
            maisFrequentes = [chr(char)]
            contagemMaisFrequente = quantidadeDaLetra
    maisFrequentes.sort()
    print(''.join(maisFrequentes))
