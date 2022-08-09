numeros = (int(input('Digite o primeiro numero : ')),
    int(input('Digite o segundo numero : ')),
    int(input('Digite o terceiro numero : ')),
    int(input('Digite o quarto numero : ')))

print(f'\nVocê digitou os valores {numeros}')
if 9 in numeros:
    print(f'O valor 9 apareceu {numeros.count(9)} vezes')
else:
    print('O valor 9 não foi digitado!')
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3) + 1}° posição')
else:
    print('O valor 3 não foi digitado!')
print(f'Os valores pares digitados foram ', end = '')
for num in numeros:
    if num % 2 == 0:
        print(f'{num} ', end = '')
