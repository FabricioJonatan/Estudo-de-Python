contador = total = 0
numeros = []

while True:
    print('Digite 0 para ver os resultados')
    numero = int(input(f'Digite o {contador+1}° número : '))
    total += numero

    if numero == 0:
        break
    if contador == 0:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    
    contador += 1
    numeros.append(numero)
    
media = total / contador

print(f'Números digitados = {numeros}')
print(f'Maior = {maior}')
print(f'Menor = {menor}')
print(f'Média = {media}')