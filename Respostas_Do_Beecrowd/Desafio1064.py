media = 0
positivos = 0
soma = 0

for c in range(1, 7):
    numero = float(input())
    
    if numero > 0:
        positivos += 1
        soma += numero
        media = soma / positivos

print('{} valores positivos'.format(positivos))
print('{:.1f}'.format(media))