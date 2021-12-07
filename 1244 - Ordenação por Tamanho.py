def geraSeparadoPorTamanho(string):
    stringSeparada = list()
    for c in range(50, 0, -1):
        for palavra in string:
            if len(palavra) == c:
                stringSeparada.append(palavra)
    return stringSeparada
    

def main():
    entrada1 = int(input())
    lista = list()
    for c in range(entrada1):
        entrada = input()
        entrada = entrada.split()
        novaString = geraSeparadoPorTamanho(entrada)
        lista.append(novaString)
    for frase in lista:
        fraseDecodificada = ''
        for palavra in frase:
            fraseDecodificada += palavra
            fraseDecodificada += ' '
        print(fraseDecodificada.strip())
main()
