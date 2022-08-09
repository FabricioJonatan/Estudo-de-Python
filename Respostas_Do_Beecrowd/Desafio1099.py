n = int(input())
soma = 0

for cont in range(1, n + 1):
    x, y = map(int, input().split())

    if x > y:
        maior = x
    else:
        maior = y
    if y < x:
        menor = y
    else:
        menor = x

    for c in range(menor + 1, maior):
        if c % 2 == 1:
            soma += c

    print(soma)
    soma = 0