entrada = int(input())
print(f'{entrada // 365} ano(s)')
entrada %= 365
print(f'{entrada // 30} mes(es)')
entrada %= 30
print(f'{entrada} dia(s)')