#   Crie um programa que vai ler vários números e colocar
# em uma lista. Depois disso, mostre:

# a) Quantos números foram digitados
# b) Se o valor 5 foi digitado















numeros = []

while True:
    numero = int(input('Digite algum numero [999 pra sair] : '))
    numeros.append(numero)

    if numero == 999:
        break

print(f'Foram digitados {len(numeros) - 1} numeros ao todo')

if 5 in numeros:
    print('O valor 5 foi digitado acima!')
else:
    print('O valor 5 não foi digitado acima!')