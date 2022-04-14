distancias = list()
while True:
    try:
        input()
        distancia = float(input())
        distancias.append(distancia)
    except EOFError:
        break

print(f'{sum(distancias) / len(distancias):.1f}')