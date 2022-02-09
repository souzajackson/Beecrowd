def enumerate_invertido(seq):
    return zip(range(len(seq) - 1, -1, -1), seq)


def main():
    while True:
        try:
            entrada = input()
            if '-' in entrada:
                entrada = entrada[1:]
            maior = sorted(entrada)[-1]
            dic = {'0': 1, '1': 2, '2': 3, '3': 4, '4': 5, '5': 6, '6': 7, '7': 8, '8': 9, '9': 10,'A':11, 'B':12, 'C':13, 'D':14, 'E':15, 'F':16, 'G':17, 'H':18, 'I':19,'J':20,'K':21,'L':22,'M':23,'N':24,'O':25,'P':26,'Q':27,'R':28,'S':29,'T':30,'U':31,'V':32,'W':33,'X':34,'Y':35,'Z':36,'a': 37, 'b': 38, 'c': 39, 'd': 40, 'e': 41, 'f': 42, 'g': 43, 'h': 44, 'i': 45, 'j': 46, 'k': 47, 'l': 48, 'm': 49, 'n': 50, 'o': 51, 'p': 52, 'q': 53, 'r': 54, 's': 55, 't': 56, 'u': 57, 'v': 58, 'w': 59, 'x': 60, 'y': 61, 'z': 62}
            base = dic[maior]
            if base < 2:
                base = 2
            for n in range(base, 64):
                valor = 0
                if n > 36:
                    for pos,e in enumerate_invertido(entrada):
                        try:
                            valor += (dic[e] - 1) * n ** pos
                        except:
                            continue 
                else:
                    valor = int(entrada, n)
                if valor % (n - 1) == 0:
                    print(n)
                    break
            else:
                print('such number is impossible!')
        except EOFError:
            break
main()
