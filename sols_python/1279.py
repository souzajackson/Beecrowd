outputs = 0
while True:
    try:
        entrada = int(input())
        if outputs > 0:
            print()
        isBissexto = False
        if entrada % 4 == 0:
            if entrada % 100 != 0 or entrada % 400 == 0:
                isBissexto = True
        if entrada % 15 == 0:
            isHuluculu = True
        else:
            isHuluculu = False
        if entrada % 55 == 0 and isBissexto:
            isBulukulu = True
        else:
            isBulukulu = False
        if isBissexto:
            print('This is leap year.')
        if isHuluculu:
            print('This is huluculu festival year.')
        if isBulukulu:
            print('This is bulukulu festival year.')
        if isHuluculu == False and isBulukulu == False and isBissexto == False:
            print('This is an ordinary year.')
        outputs += 1
    except EOFError:
        break
