entrada1 = int(input())
lista = list()
for c in range(entrada1):
    entrada = input()
    lista.append(entrada)
for sequencia in lista:
    string = sequencia.replace('.', '')
    quantidadeDeDiamantes = 0
    while string.count('<>') != 0:
        quantidadeDeDiamantes += string.count('<>')
        string = string.replace('<>', '')
    print(quantidadeDeDiamantes)
    