while True:
    try:
        entrada = input()
        if entrada == '0':
            break
        entrada = list(range(int(entrada)))
        entradaCopia = entrada.copy()
        m = 1
        while True:
            entrada.pop(0)
            atual = -1
            while len(entrada) > 1:
                atual += m
                while atual > len(entrada) - 1:
                    atual -= len(entrada)
                entrada.pop(atual)
                atual -= 1
            if entrada[0] == 12: break
            m += 1
            entrada = entradaCopia.copy()

        print(m)
    except:
        break
