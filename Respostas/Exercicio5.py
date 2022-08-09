#   Crie um programa onde o usuário possa digitar 7
# valores numéricos e coloque-os em uma lista única que
# mantenha separados os valores pares e ímpares. No final
# mostre os valores pares e ímpares.



















numeros = [[], []]

for i in range(7):
    numero = int(input('Digite um numero qualquer :'))
    
    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)

print(f'Os numeros pares digitados foram {numeros[0]}')
print(f'Os numeros impares digitados foram {numeros[1]}')