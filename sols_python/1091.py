while True:
    entrada = int(input())
    if entrada == 0:
        break
    divisa = input().split()
    for pos, elemento in enumerate(divisa):
        divisa[pos] = int(elemento)
    for c in range(entrada):
        consulta = input().split()
        for pos, elemento in enumerate(consulta):
            consulta[pos] = int(elemento)
        if consulta[0] == divisa[0] or consulta[1] == divisa[1]:
            print('divisa')
        elif consulta[0] > divisa[0] and consulta[1] > divisa[1]:
            print('NE')
        elif consulta[0] > divisa[0] and consulta[1] < divisa[1]:
            print('SE')
        elif consulta[0] < divisa[0] and consulta[1] < divisa[1]:
            print('SO')
        else:
            print('NO')
