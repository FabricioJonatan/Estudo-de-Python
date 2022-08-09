#   Desenvolva um programa que leia 4 valores
# e guarde-os em uma lista. No final, mostre:

# a) Quantas vezes apareceu o numero 9
# b) Quantas vezes apareceu o numero 3
# c) Quais numeros são pares













numeros = []
pares = []
numerotres = numeronove = 0

for i in range(4):
    numero = int(input('Digite um numero : '))
    numeros.append(numero)

for numero in numeros:
    if numero == 3:
        numerotres = numerotres + 1
    if numero == 9:
        numeronove = numeronove + 1
    if numero % 2 == 0:
        pares.append(numero)

print(f'O numero 9 foi digitado {numeronove} vezes')
print(f'O numero 3 foi digitado {numerotres} vezes')
print(f'Os numeros pares digitados foram {pares}')