while True:
    x, y = map(int, input().split())

    if x > y:
        ordem = 'Decrescente'
    elif x < y:
        ordem = 'Crescente'
    else:
        break

    print(ordem)