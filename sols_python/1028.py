entrada = int(input())
for c in range(entrada):
    entrada = input().split()
    entrada[0] = int(entrada[0])
    entrada[1] = int(entrada[1])
    while True:
        calculo = max(entrada) % min(entrada)
        if calculo == 0:
            print(min(entrada))
            break
        else:
            entrada[0] = min(entrada)
            entrada[1] = calculo
