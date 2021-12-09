while True:
    try:
        entrada = input().split()

        distanciaPercorrida = int(entrada[0]) * int(entrada[1]) * 2
        print(distanciaPercorrida)
    except EOFError:
        break