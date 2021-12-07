def adicionaParaArena(char):
    global arena
    global posicaoRobo
    global orientacaoAtual
    arena.append(char)
    if char in 'NLSO':
        posicaoRobo = arena.index(char)
        orientacaoAtual = char


def fazerMovimento(movimento):
    global arena
    global posicaoRobo
    global posicoes
    global orientacaoAtual
    global movimentacoes
    global figurasColetadas
    global ultimasPosicoes
    global primeirasPosicoes
    if movimento == 'E':
        if posicoes.index(orientacaoAtual) - 1 >= 0:
            arena[posicaoRobo] = posicoes[posicoes.index(orientacaoAtual) - 1]
            orientacaoAtual = posicoes[posicoes.index(orientacaoAtual) - 1]
        else:
            arena[posicaoRobo] = 'O'
            orientacaoAtual = 'O'
    elif movimento == 'D':
        if posicoes.index(orientacaoAtual) + 1 <= 3:
            arena[posicaoRobo] = posicoes[posicoes.index(orientacaoAtual) + 1]
            orientacaoAtual = posicoes[posicoes.index(orientacaoAtual) + 1]
        else:
            arena[posicaoRobo] = 'N'
            orientacaoAtual = 'N'
    elif movimento == 'F':
        deslocamento = movimentacoes[orientacaoAtual]
        movimentoIsValido = True
        if orientacaoAtual == 'L' and posicaoRobo in ultimasPosicoes:
            movimentoIsValido = False
        elif orientacaoAtual == 'O' and posicaoRobo in primeirasPosicoes:
            movimentoIsValido = False
        if movimentoIsValido:
            if 0 <= posicaoRobo + deslocamento < len(arena):
                if arena[posicaoRobo + deslocamento] != '#':
                    if arena[posicaoRobo + deslocamento] == '*':
                        figurasColetadas += 1
                    arena[posicaoRobo] = '.'
                    arena[posicaoRobo + deslocamento] = orientacaoAtual
                    posicaoRobo += deslocamento


while True:
    figurasColetadas = 0
    entrada = input().split()
    arena = []
    orientacaoAtual = ''
    posicaoRobo = ''
    posicoes = ['N', 'L', 'S', 'O']
    movimentacoes = {
        'N': -int(entrada[1]),
        'L': 1,
        'S': int(entrada[1]),
        'O': -1
    }
    if entrada == ['0', '0', '0']:
        break
    for c in range(int(entrada[0])):
        novaLinha = input()
        criacaoArena = list(map(adicionaParaArena, novaLinha))
    primeirasPosicoes = list(range(0, len(arena), int(entrada[1])))
    ultimasPosicoes = list(range(int(entrada[1]) - 1, len(arena), int(entrada[1])))
    movimentos  = input()
    fazerMovimentos = list(map(fazerMovimento, movimentos))
    print(figurasColetadas)
