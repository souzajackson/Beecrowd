while True:
    entrada = input().split()
    if entrada == ['0', '0']:
        break
    G = int(entrada[0])
    P = int(entrada[1])
    pilotos = dict()

    for corrida in enumerate(range(G)):
        for pos, ordem_chegada in enumerate([int(n) for n in input().split()]):
            if pos + 1 in pilotos:
                pilotos[pos + 1].append(ordem_chegada)
            else:
                pilotos[pos + 1] = [ordem_chegada]
    
    S = int(input())
    for sistema in range(S):
        pontuadores = dict()
        sistema_pontuacao = [int(n) for n in input().split()[1:]]
        for pos1, piloto in enumerate(pilotos.values()):
            for pos2, pontuacao in enumerate(sistema_pontuacao):
                if pos2 + 1 in set(piloto):
                    if pos1 + 1 in pontuadores:
                        pontuadores[pos1 + 1] += piloto.count(pos2 + 1) * pontuacao
                    else:
                        pontuadores[pos1 + 1] = piloto.count(pos2 + 1) * pontuacao
        maior_pontuacao = max(pontuadores.values())
        vencedores = ''
        for piloto in pontuadores:
            if pontuadores[piloto] == maior_pontuacao:
                vencedores += f'{piloto} '
        print(vencedores[:-1])
