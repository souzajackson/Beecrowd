quantidadeDeTestes = int(input())
for c in range(quantidadeDeTestes):
    entrada = input()
    mensagemComPasso1 = '' 
    for letra in entrada:
        if 97 <= ord(letra) <= 122 or 65 <= ord(letra) <= 90:
            mensagemComPasso1 += chr(ord(letra) + 3)
        else:
            mensagemComPasso1 += letra
    mensagemComPasso2 = mensagemComPasso1[::-1]
    metadeDaMensagem = int(len(mensagemComPasso2) / 2)
    mensagemFinal = ''
    for c in range(0, metadeDaMensagem):
        mensagemFinal += mensagemComPasso2[c]
    for c in range(metadeDaMensagem, len(mensagemComPasso2)):
        mensagemFinal += chr(ord(mensagemComPasso2[c]) - 1)
    print(mensagemFinal)