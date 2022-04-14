while True:
    entrada = input()
    if entrada == '*':
        break
    entrada = entrada.split()
    primeiraLetra = entrada[0][0].upper()
    ok = True
    for palavra in entrada:
        if palavra[0].upper() != primeiraLetra:
            ok = False
            break
    if ok:
        print('Y')
    else:
        print('N')