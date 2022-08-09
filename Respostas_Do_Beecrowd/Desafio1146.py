lista = []

while True:
    n = int(input())

    if n == 0:
        break

    for c in range(1, n + 1):
        lista.append(c)
        lista[c - 1] = str(lista[c - 1])

    lista = ' '.join(lista)
    print(lista)
    lista = []
