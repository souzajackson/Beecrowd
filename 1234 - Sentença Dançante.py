while True:
    try:
        entrada = input()
        alternancia = 0
        fraseDancante = ''
        for char in entrada:
            if char == ' ':
                fraseDancante += ' '
                continue
            else:
                fraseDancante += char.upper() if alternancia % 2 == 0 else char.lower()
            alternancia += 1
        print(fraseDancante)
    except EOFError:
        break
