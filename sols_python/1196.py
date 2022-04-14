def checar(string):
    for letra in string:
            if letra == ' ':
                return ' '
            else:
                if letra in linha1:
                    return linha1[linha1.index(letra) - 1]
                elif letra in linha2:
                    return linha2[linha2.index(letra) - 1]
                elif letra in linha3:
                    return linha3[linha3.index(letra) - 1]
                elif letra in linha4:
                    return linha4[linha4.index(letra) - 1]


linha1 = ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=']
linha2 = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', '\\']
linha3 = ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', "'"]
linha4 = ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/']
while True:
    try:
        entrada = input()
        saida = map(checar, entrada)
        print(''.join(saida))
    except EOFError:
        break
