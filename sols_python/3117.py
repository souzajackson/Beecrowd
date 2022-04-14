entrada1 = input().split()
entrada1[0] = int(entrada1[0])
entrada1[1] = int(entrada1[1])
entrada2 = input().split()
for pos, elemento in enumerate(entrada2):
    entrada2[pos] = int(elemento)
atrasados = 0
entrada2.sort()
for atraso in entrada2:
    if atraso > 0:
        atrasados += 1
if entrada1[0] - atrasados >= entrada1[1]:
    print('YES')
else:
    print('NO')
    