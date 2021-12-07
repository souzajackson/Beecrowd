entrada = int(input())

for c in range(entrada):
    desafio = input()
    if desafio[0] == desafio[2]:
        print(int(desafio[0]) ** 2)
    elif desafio[1].isupper():
        print(int(desafio[2]) - int(desafio[0]))
    else:
        print(int(desafio[2]) + int(desafio[0])) 
