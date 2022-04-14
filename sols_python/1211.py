while True:
    try:
        quantidadeDeNumerosDeTelefone = int(input())
        telefones = list()
        economia = 0
        for c in range(quantidadeDeNumerosDeTelefone):
            numeroDoTelefone = input()
            telefones.append(numeroDoTelefone)
        
        for posLista, telefone in enumerate(telefones):
            if posLista == 0:
                continue
            for posTelefone, numero in enumerate(telefone):
                if numero == telefones[posLista - 1][posTelefone]:
                    economia += 1
                else:
                    break
        print(economia)
    except EOFError:
        break
