dicionario = {
    '1': 2,
    '2': 5,
    '3': 5,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 3,
    '8': 7,
    '9': 6,
    '0': 6
}
entrada = int(input())
for c in range(entrada):
    teste = input()
    ledsNecessarios = 0
    for numero in teste:
        ledsNecessarios += dicionario[numero]
    print(f'{ledsNecessarios} leds')
