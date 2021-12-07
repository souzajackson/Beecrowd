dicionario = {
    'a': 10,
    'b': 11,
    'c': 12,
    'd': 13,
    'e': 14,
    'f': 15
}
while True:
    entrada = input()
    try:
        int(entrada)
    except:
        entrada = entrada[2:]
    else:
        if int(entrada) < 0:
            break
        saida = ''
        saida += '0x'
        saida += hex(int(entrada))[2:].upper()
        print(saida)
        continue
    expoente = len(entrada) - 1
    decimal = 0
    for numero in entrada:
        try:
            int(numero)
        except:
            numeroAtual = dicionario[numero]
        else:
            numeroAtual = int(numero)
        decimal += 16 ** expoente * numeroAtual
        expoente -= 1
    print(decimal)
