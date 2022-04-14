while True:
    entrada = input().split('/')
    if entrada == ['*']:
        break
    duracoes = {
        'W': 1,
        'H': 1 / 2,
        'Q': 1 / 4,
        'E': 1 / 8,
        'S': 1 / 16,
        'T': 1 / 32,
        'X': 1 / 64 
    }
    compassosCertos = 0
    for compasso in entrada:
        duracaoTotal = 0
        for nota in compasso:
            duracaoTotal += duracoes[nota]
        if duracaoTotal == 1:
            compassosCertos += 1
    print(compassosCertos)
