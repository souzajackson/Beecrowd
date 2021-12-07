from math import hypot
while True:
    try:
        entrada = input().split()
        lado1 = 12
        lado2 = int(entrada[0])
        lado3 = hypot(lado1, lado2)
        tempoPolicia = lado3 / int(entrada[2])
        tempoLadrao = lado1 / int(entrada[1])
        if tempoPolicia <= tempoLadrao:
            print('S')
        else:
            print('N') 
    except EOFError:
        break
