entrada = int(input())
for c in range(entrada):
    dieta = list(input())
    cafe = list(input())
    almoco = list(input())
    erros = 0
    for comida in cafe:
        if comida in dieta:
            dieta.remove(comida)
        else:
            erros += 1
    for comida in almoco:
        if comida in dieta:
            dieta.remove(comida)
        else:
            erros += 1
    if erros == 0:
        for comida in sorted(dieta):
            if len(dieta) > 0:
                print(f'{comida}', end='')
        print()
    else:
        print('CHEATER')
