entrada = int(input())
for c in range(entrada):
    entrada = input().strip().split()
    palavraCodificada = ''
    for palavra in entrada:
        palavraCodificada += palavra[0]
    print(palavraCodificada)
