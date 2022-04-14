while True:
    entrada = input().split()

    if entrada == ['0', '0']:
        break
    entrada = list(map(int, entrada))
    entrada.sort()
    entrada = list(map(str, entrada))
    carrys = 0
    carrysAguardando = 0
    for c in range(len(entrada[0])):
        if int(entrada[0][-c - 1]) + int(entrada[1][-c -1]) + carrysAguardando >= 10:
            carrys += 1
            carrysAguardando = 1
        else:
            carrysAguardando = 0
    if len(entrada[1]) > len(entrada[0]):
        posAtual = len(entrada[1]) -c - 2
        for i in range(posAtual, -1, -1):
            if int(entrada[1][i]) == 9 and carrysAguardando == 1:
                carrys += 1
            else:
                break
    
    if carrys == 0:
        print('No carry operation.')
    elif carrys == 1:
        print(f'{carrys} carry operation.')
    else:
        print(f'{carrys} carry operations.')
