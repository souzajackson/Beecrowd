from sys import stdin
for entrada in stdin.readlines()[:-1]:
    seq = [int(n) - 1 for n in entrada.split()[1:]]
    ordenado = sorted(seq)
    jogadasFeitas = 0
    while True:
        if seq == ordenado:
            break
        for atual, certo in zip(seq, ordenado):
            if atual != certo:
                seq[atual], seq[certo] = seq[certo], seq[atual]
                jogadasFeitas += 1
    print('Carlos' if jogadasFeitas % 2 == 0 else 'Marcelo')
