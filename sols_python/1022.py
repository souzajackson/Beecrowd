def transformaInteiro(termo):
    try:
        return int(termo)
    except:
        return termo


quantidadeDeTestes = int(input())

for c in range(quantidadeDeTestes):
    expressão = input().split()
    expressão = list(map(transformaInteiro, expressão))

    if expressão[3] == '+':
        mmc = expressão[2] * expressão[6]
        expressão[0] *= expressão[6]
        expressão[4] *= expressão[2]
        resultado = f'{expressão[0] + expressão[4]} / {mmc}'.split()
    elif expressão[3] == '-':
        mmc = expressão[2] * expressão[6]
        expressão[0] *= expressão[6]
        expressão[4] *= expressão[2]
        resultado = f'{expressão[0] - expressão[4]} / {mmc}'.split()
    elif expressão[3] == '*':
        resultado = f'{expressão[0] * expressão[4]} / {expressão[2] * expressão[6]}'.split()
    elif expressão[3] == '/':
        numeradorAntigo = expressão[4]
        expressão[4] = expressão[6]
        expressão[6] = numeradorAntigo
        resultado = f'{expressão[0] * expressão[4]} / {expressão[2] * expressão[6]}'.split()

    print(''.join(resultado), end=' = ')

    resultado[0] = int(resultado[0])
    resultado[2] = int(resultado[2])
    divisoresDoDenonimador = list()
    for c in range(2, resultado[2] + 1):
        if resultado[2] % c == 0:
            divisoresDoDenonimador.append(c) 
    while True:
        divisoesFeitas = 0
        for c in reversed(divisoresDoDenonimador):
            if resultado[0] % c == 0 and resultado[2] % c == 0:
                resultado[0] //= c
                resultado[2] //= c
                divisoesFeitas += 1
        if divisoesFeitas == 0:
            break
    resultadoFinal = f'{resultado[0]}{resultado[1]}{resultado[2]}'

    print(resultadoFinal)
