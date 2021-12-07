entrada = int(input())
for c in range(entrada):
    dietaLista = list()
    cafeLista = list()
    almocoLista = list()
    dieta = input()
    cafe = input()
    almoco = input()
    for comida in dieta:
        dietaLista.append(comida)
    for comida in cafe:
        cafeLista.append(comida)
    for comida in almoco:
        almocoLista.append(comida)
    erros = 0
    for comida in cafeLista:
        if comida in dietaLista:
            dietaLista.remove(comida)
        else:
            erros += 1
    for comida in almocoLista:
        if comida in dietaLista:
            dietaLista.remove(comida)
        else:
            erros += 1
    if erros == 0:
        for comida in sorted(dietaLista):
            if len(dietaLista) > 0:
                print(f'{comida}', end='')
        print()
    else:
        print('CHEATER')
