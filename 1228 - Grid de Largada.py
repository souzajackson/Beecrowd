while True:
    try:
        numero_de_corredores = int(input())
        grid_de_largada = input().split()
        grid_de_chegada = input().split()
        
        ultrapassagens = 0
        grid_processamento = grid_de_largada.copy()
        while grid_processamento != grid_de_chegada:
            for pos, corredor in enumerate(grid_de_chegada):
                if pos < grid_processamento.index(corredor):
                    ultrapassagens += grid_processamento.index(corredor) - pos
                    grid_processamento.remove(corredor)
                    grid_processamento.insert(pos, corredor)

        print(ultrapassagens)
    except EOFError:
        break
