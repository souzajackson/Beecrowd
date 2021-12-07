def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)
        
        
while True:
    try:
        entrada = input()
        entrada = entrada.split()
        fat1 = fatorial(int(entrada[0]))
        fat2 = fatorial(int(entrada[1]))
        print(fat1 + fat2)
    except EOFError:
        break