while True:
    try:
        input()
        alice = set(input().split())
        beatriz = set(input().split())
        repeticoes = [1 for carta in alice if carta in beatriz]
        print(min([len(alice), len(beatriz)]) - len(repeticoes))
    except EOFError:
        break
