def porrada(seq, passo):
    atual = 0
    while len(seq) > 1:
        atual += passo - 1
        while atual > len(seq) - 1:
            atual -= len(seq) 
        seq.pop(atual)
    return seq[0] + 1
quantidade_de_casos = int(input())
for c in range(quantidade_de_casos):
    entrada = input().split()

    n = list(range(int(entrada[0])))
    m = int(entrada[1])

    print(f'Case {c + 1}: {porrada(n, m)}')
