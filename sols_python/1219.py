from math import pi, sqrt
while True:
    try:
        lados = input().split()
        lado1 = int(lados[0])
        lado2 = int(lados[1])
        lado3 = int(lados[2])

        perimetro = lado1 + lado2 + lado3
        p = perimetro / 2
        area_do_triangulo = sqrt(p * (p - lado1) *  (p - lado2) * (p - lado3))

        raio_circulo_maior = lado3 * lado2 * lado1 / (4 * area_do_triangulo)
        area_circulo_maior = pi * raio_circulo_maior ** 2 - area_do_triangulo

        raio_circulo_menor = area_do_triangulo / p
        area_circulo_menor = pi * raio_circulo_menor ** 2
        area_do_triangulo -= area_circulo_menor

        print(f'{area_circulo_maior:.4f} {area_do_triangulo:.4f} {area_circulo_menor:.4f}')
    except EOFError:
        break
