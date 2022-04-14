entrada = int(input())
cedulas = [100, 50, 20, 10, 5, 2, 1]
print(entrada)
for cedula in cedulas:
    cedulasNecessarias = entrada // cedula
    print(f'{cedulasNecessarias} nota(s) de R$ {cedula},00')
    entrada %= cedula
