#   Crie um programa que vai pedir 5 numeros
# aleatórios e coloque em uma lista. Mostre os
# numeros digitados e também mostre o maior e
# menor valor que foi digitado


















numeros = []

for i in range(5):
    numero = int(input('Digite um número : '))
    numeros.append(numero)

for num in range(len(numeros)):
    if num == 0:
        maior = numeros[num]
        menor = numeros[num]
    else:
        if maior < numeros[num]:
            maior = numeros[num]
        if menor > numeros[num]:
            menor = numeros[num]

print(f'Os numeros digitados foram {numeros}')
print(f'O maior numero digitado foi {maior}')
print(f'O menor numero digitado foi {menor}')