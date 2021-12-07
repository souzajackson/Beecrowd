while True:
    try:
        sequencia = input()
        processosSimultaneos = int(input())

        ciclos = 0
        ciclos += sequencia.count('R' * processosSimultaneos)
        sequencia = sequencia.replace('R' * processosSimultaneos, '')
        for pos, char in enumerate(sequencia):
            if pos == len(sequencia) - 1:
                ciclos += 1
            else:
                if char == 'R':
                    if sequencia[pos + 1] == 'W':
                        ciclos += 1
                elif char == 'W':
                    ciclos += 1

        print(ciclos)
    except EOFError:
        break
