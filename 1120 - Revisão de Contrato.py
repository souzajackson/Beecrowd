while True:
    entrada = input().split()
    if entrada == ['0', '0']:
        break
    tecla_com_defeito = entrada[0]
    numero_esperado = entrada[1]
    numero_digitado = numero_esperado.replace(tecla_com_defeito, '')
    if numero_digitado == '':
        print(0)
    else:
        print(int(numero_digitado))
