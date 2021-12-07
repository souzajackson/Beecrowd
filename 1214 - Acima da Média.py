entrada1 = int(input())
lista = list()
for c in range(entrada1):
    entrada = input()
    entrada = entrada.split()
    entrada.pop(0)
    for pos, elemento in enumerate(entrada):
        entrada[pos] = int(elemento)
    lista.append(entrada)
for turma in lista:
    alunosAcimaDaMedia = 0
    somaTotal = 0
    for nota in turma:
        somaTotal += nota
    media = somaTotal / len(turma)
    for nota in turma:
        if nota > media:
            alunosAcimaDaMedia += 1
    print(f'{(alunosAcimaDaMedia / len(turma)) * 100:.3f}%')
    