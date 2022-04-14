while True:
    try:
        entrada = int(input())
        print('Y' if entrada % 6 == 0 else 'N')
    except:
        break