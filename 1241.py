quantidade_testes = int(input())

for c in range(quantidade_testes):
    entrada = input().split()
    if entrada[0][len(entrada[0]) - len(entrada[1]):] == entrada[1]:
        print('encaixa')
    else:
        print('nao encaixa')
