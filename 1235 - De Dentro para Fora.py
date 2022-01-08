quantidade_de_casos = int(input())

for c in range(quantidade_de_casos):
    frase = input()
    centro = len(frase) // 2
    primeiraParte = list(reversed(frase[:centro]))
    segundaParte = list(reversed(frase[centro:]))
    output = ''.join(primeiraParte) + ''.join(segundaParte)
    
    print(output)