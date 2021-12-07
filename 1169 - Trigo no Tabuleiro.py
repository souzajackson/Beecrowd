while True:
    try:
        entrada = int(input())
        for c in range(entrada):
            teste = int(input())
            soma = 0
            for expoente in range(teste):
                soma += 2 ** expoente
            print(f'{int(soma / 12 /1000 // 1)} kg')
    except EOFError:
        break
