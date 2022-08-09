positivos = 0

for c in range(1,7):
    valor = float(input())
    if valor > 0:
        positivos += 1

print('{} valores positivos'.format(positivos))