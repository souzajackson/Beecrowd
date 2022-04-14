horas = list(range(24))
lista = list()
while True:
    try:
        entrada = input()
        if entrada == '0 0 0 0':
            break
        entrada = entrada.split()
        for pos, elemento in enumerate(entrada):
            entrada[pos] = int(elemento)
        lista.append(entrada)
    except EOFError:
        break
lista.pop()
for horarios in lista:
    if horarios[0] * 60 + horarios[1] <= horarios[2] * 60 + horarios[3]:
        horarios[0] *= 60
        horarios[2] *= 60
        print(abs(horarios[0] + horarios[1] - horarios[2] - horarios[3]))
    else:
        minutosAdicionados = 0
        while True:
            horarios[0] += 1
            minutosAdicionados += 60
            if horarios[0] == 24:
                horarios[0] = 0
            if horarios[0] == horarios[2]:
                if horarios[1] > horarios[3]:
                    minutosAdicionados -= horarios[1] - horarios[3]
                    break
                elif horarios[1] < horarios[3]:
                    minutosAdicionados += horarios[3] - horarios[1]
                    break
                else:
                    break
        print(minutosAdicionados)
            