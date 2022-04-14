quantidade_habilidades, quantidade_texto = [int(n) for n in input().split()]

dicionario = dict()
for c in range(quantidade_habilidades):
    habilidade_descricao = input().split()
    dicionario[habilidade_descricao[0]] = float(habilidade_descricao[1])

for c in range(quantidade_texto):
    salario = 0 
    while True:
        linha = input()
        for palavra in linha.split():
            if palavra in dicionario.keys():
                salario += dicionario[palavra]
        if linha == '.':
            break
    print(int(salario))
