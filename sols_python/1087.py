lista = list()
while True:
    entrada = input()
    if entrada == '0 0 0 0':
        break
    entrada = entrada.split()
    for pos, elemento in enumerate(entrada):
        entrada[pos] = int(elemento)
    posicaoAtual = entrada[0:2]
    posicaoFinal = entrada[2:]
    posicao = [posicaoAtual, posicaoFinal]
    lista.append(posicao)
for posicao in lista:
    if posicao[0] == posicao[1]:
        print(0)
    elif posicao[0][0] == posicao[1][0] or posicao[0][1] == posicao[1][1]:
        print(1)
    elif abs(posicao[0][0] - posicao[1][0]) == abs(posicao[0][1] - posicao[1][1]):
        print(1)
    else:
        print(2) 
        