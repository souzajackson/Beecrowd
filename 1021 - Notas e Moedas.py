notas = [100, 50, 20, 10, 5, 2]
moedas = [100, 50, 25, 10, 5, 1]
entrada = float(input())
print('NOTAS:')
for nota in notas:
    notasNecessarias = entrada // nota
    print(f'{int(notasNecessarias)} nota(s) de R$ {nota:.2f}')
    if notasNecessarias != 0:
        entrada %= notasNecessarias * nota
print('MOEDAS:')
entrada *= 100
for moeda in moedas:
    moedasNecessarias = entrada // moeda
    print(f'{int(moedasNecessarias)} moeda(s) de R$ {moeda / 100:.2f}')
    if moedasNecessarias != 0:
        entrada %= moedasNecessarias * moeda
