while True:
    try:
        entrada = input()
        entrada = entrada.replace(' .', '.')
        entrada = entrada.replace(' ,', ',')
        print(entrada)
    except EOFError:
        break
    