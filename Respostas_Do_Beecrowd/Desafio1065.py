pares = 0

for c in range(1, 6):
    numero = int(input())

    if numero % 2 == 0:
        pares += 1

print('{} valores pares'.format(pares))