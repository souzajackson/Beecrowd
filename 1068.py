def eliminaLetra(char):
    if char != '(' and char != ')':
        return ''
    else:
        return char


while True:
    try:
        entrada = map(eliminaLetra, input())
        abertos = 0 
        for char in entrada:
            if char == '(':
                abertos += 1
            elif char == ')' and abertos == 0:
                raise ValueError
            elif char == ')' and abertos > 0:
                abertos -= 1
        if abertos > 0:
            raise ValueError            
    except EOFError:
        break
    except:
        print('incorrect')
    else:
        print('correct')