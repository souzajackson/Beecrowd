while True:
    entrada = input().split()
    if entrada == ['0', '0']:
        break
    N = int(entrada[0])
    bolas_restantes = set([int(n) for n in input().split()])

    numeros_totais = range(0, N + 1)
    possiveis = []
    for bola in numeros_totais:
        for restante in bolas_restantes:
            if abs(bola - restante) in bolas_restantes and bola + abs(bola - restante) in bolas_restantes:
                possiveis.append(bola)
                break
        else:
            break

    print('Y' if len(possiveis) == len(numeros_totais) else 'N')
