entrada = int(input())
horas = entrada // 3600
entrada %= 3600
minutos = entrada // 60
entrada %= 60
segundos = entrada
print(f'{horas}:{minutos}:{segundos}')