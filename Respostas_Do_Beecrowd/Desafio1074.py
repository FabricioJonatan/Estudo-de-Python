quantidade = int(input())

for c in range(quantidade):
    numero = int(input())
    if numero != 0:
        if numero % 2 == 0:
            print('EVEN ', end = '')
            if numero > 0:
                print('POSITIVE')
            else:
                print('NEGATIVE')
        else:
            print('ODD ', end = '')
            if numero > 0:
                print('POSITIVE')
            else:
                print('NEGATIVE')
    else:
        print('NULL')