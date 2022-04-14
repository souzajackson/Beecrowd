while True:
    try:
        entrada = input().split()
        entrada = [int(n) for n in entrada]
        numero_palavras = entrada[0]
        linhas_pagina = entrada[1]
        caracteres_linha = entrada[2]
        texto = input()

        texto += ' '
        linhas_usadas = 0
        inicio = 0
        while True:
            cont = 0
            while cont <= caracteres_linha and inicio + cont < len(texto):
                cont += 1
            
            inicio += cont - 1
            if texto[inicio].isalpha():
                if texto[inicio] == ' ':
                    inicio += 2
                else:
                    while texto[inicio - 1].isspace() == False:
                        inicio -= 1
            elif texto[inicio].isspace():
                inicio += 1
            linhas_usadas += 1
            if inicio > len(texto) - 1:
                break

        if linhas_usadas / linhas_pagina == int(linhas_usadas / linhas_pagina):
            paginas_usada = int(linhas_usadas / linhas_pagina) 
        else:
            paginas_usada = int(linhas_usadas / linhas_pagina) + 1

        print(paginas_usada)
    except EOFError:
        break
