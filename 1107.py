def main():
    while True:
        entrada = input()
        if entrada == '0 0': break
        altura = int(entrada.split()[0])
        formato_final = [int(n) for n in input().split()]

        laserUsados = 0
        for pos, valor_inicial in enumerate(formato_final):
            if pos == 0:
                laserUsados += altura - valor_inicial
            elif valor_inicial < formato_final[pos - 1]:
                laserUsados += formato_final[pos - 1] - valor_inicial
 
        print(laserUsados)
main()
