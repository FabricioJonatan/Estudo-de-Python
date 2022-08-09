quant = int(input())

for c in range(1, quant + 1):
    x, y = map(int, input().split())

    if y == 0:
        print('divisao impossivel')
    else:
        divisao = x / y
        print('{:.1f}'.format(divisao))