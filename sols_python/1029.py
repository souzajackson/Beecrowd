entrada = input()
for c in range(int(entrada)):
    numero = int(input())

    numcalls = 0
    chamadas_registradas = list()
    termos = list()
    for c in range(0, numero):
        if c == 0:
            chamadas_registradas.append(0)
            termos.append(0)
        elif c == 1:
            chamadas_registradas.append(0)
            termos.append(1)
        else:
            chamadas = chamadas_registradas[c - 1] + chamadas_registradas[c - 2] + 2
            chamadas_registradas.append(chamadas)
            termos.append(termos[c - 1] + termos[c - 2])
    numcalls += chamadas_registradas[-1] + chamadas_registradas[-2] + 2
    fib = termos[-1] + termos[-2]

    print(f'fib({numero}) = {numcalls} calls = {fib}')
