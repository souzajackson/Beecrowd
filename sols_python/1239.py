while True:
    try:
        entrada = input()
        saida = ''
        tags_b = 0
        tags_i = 0 
        for char in entrada:
            if char == '*':
                tags_b += 1
                if tags_b % 2 != 0:
                    saida += '<b>'
                else:
                    saida += '</b>'
            elif char == '_':
                tags_i += 1
                if tags_i % 2 != 0:
                    saida +='<i>'
                else:
                    saida += '</i>'
            else:
                saida += char
        print(saida)
    except EOFError:
        break
