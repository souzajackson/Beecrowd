def somaErrada(n1, n2):
    global resultado
    if int(n1) + int(n2) == 1:
        return '1'
    else:
        return '0'


while True:
        try:
            entrada = input().split()
            entrada[0] = int(entrada[0])
            entrada[1] = int(entrada[1])
            entrada.sort()
            entrada[1] = bin(entrada[1])[2:]
            entrada[0] = bin(entrada[0])[2:]
            if len(entrada[1]) > len(entrada[0]):
                entrada[0] = '0' * (len(entrada[1]) - len(entrada[0])) + entrada[0]
            resultado = list(map(somaErrada, entrada[0], entrada[1]))
            print(int(''.join(resultado), 2))
        except EOFError:
            break