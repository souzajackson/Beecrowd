while True:
    entrada = input()
    if entrada == '0':
        break
    entrada = input()
    joao = entrada.count('1')
    maria = entrada.count('0')
    print(f'Mary won {maria} times and John won {joao} times')
