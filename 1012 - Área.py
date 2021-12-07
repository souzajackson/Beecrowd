entrada = input()
lista = entrada.split()
for pos, elemento in enumerate(lista):
    lista[pos] = float(elemento)
print(f'TRIANGULO: {(lista[0] * lista[2]) / 2:.3f}')
print(f'CIRCULO: {lista[2] ** 2 * 3.14159:.3f}')
print(f'TRAPEZIO: {(lista[0] + lista[1]) * lista[2] / 2:.3f}')
print(f'QUADRADO: {lista[1] ** 2:.3f}')
print(f'RETANGULO: {lista[0] * lista[1]:.3f}')