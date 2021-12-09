while True:
    try:
        entrada = sorted(list(input().replace(' ', '')))
        entrada = list(map(ord, entrada))
        entrada.append(127)
        intervalos = list()
        comecoDoIntervalo = 0
        for pos, char in enumerate(entrada):
            if pos != len(entrada) - 1:
                if entrada[pos + 1] <= char + 1:
                    continue
                intervalos.append(f'{chr(entrada[comecoDoIntervalo])}:{chr(char)}')
                comecoDoIntervalo = pos + 1
        print(', '.join(intervalos))
    except EOFError:
        break
