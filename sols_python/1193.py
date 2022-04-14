entrada = int(input())
for c in range(entrada):
    numero = input().split()
    print(f'Case {c + 1}:')
    if numero[1] == 'bin':
        print(f'{int(numero[0], 2)} dec')
        print(f'{hex(int(numero[0], 2))[2:]} hex')
    elif numero[1] == 'hex':
        print(f'{int(numero[0], 16)} dec')
        print(f'{bin(int(numero[0], 16))[2:]} bin')
    elif numero[1] == 'dec':
        print(f'{hex(int(numero[0]))[2:]} hex')
        print(f'{bin(int(numero[0]))[2:]} bin')
    print()
