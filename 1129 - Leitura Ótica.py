lista = list()
letras = ['A', 'B', 'C', 'D', 'E']
while True:
    entrada1 = input()
    if entrada1 == '0':
        break
    for c in range(int(entrada1)):
        entrada = input().split()
        for pos, elemento in enumerate(entrada):
            entrada[pos] = int(elemento)
        lista.append(entrada)
for questao in lista:
    questoesMarcadas = 0
    for alternativa in questao:
        if alternativa <= 127:
            questoesMarcadas += 1
    if questoesMarcadas == 1:
        for pos, alternativa in enumerate(questao):
            if alternativa <= 127:
                print(letras[pos])
    else:
        print('*')
        