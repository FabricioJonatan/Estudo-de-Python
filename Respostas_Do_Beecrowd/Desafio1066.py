par = 0
impar = 0 
negativo = 0
positivo = 0

for c in range(1, 6):
    numero = int(input())
    if numero % 2 == 0:
        par += 1
    if numero % 2 == 1:
        impar += 1
    if numero > 0:
        positivo += 1
    if numero < 0:
        negativo += 1

print('{} valor(es) par(es)'.format(par))
print('{} valor(es) impar(es)'.format(impar))
print('{} valor(es) positivo(s)'.format(positivo))
print('{} valor(es) negativo(s)'.format(negativo))