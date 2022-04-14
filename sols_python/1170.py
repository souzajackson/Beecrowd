entrada = int(input())
for c in range(entrada):
    quantidadeDeComida = float(input())
    diasComendo = 0
    while True:
        if quantidadeDeComida <= 1:
            break
        quantidadeDeComida /= 2
        diasComendo += 1
    print(f'{diasComendo} dias')
