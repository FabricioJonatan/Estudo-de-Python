numeros = [[],[]]

for valores in range(7):
    numero = int(input(f'Digite o {valores + 1}° valor : '))

    if numero % 2 == 0:
        if numero != 0:
            numeros[1].append(numero)
    else:
        numeros[0].append(numero)
    
if len(numeros[0]) > 0:
    print(f'Os valores IMPARES digitados foram {sorted(numeros[0])}!')
else:
    print('Não foi digitado nenhum valor IMPAR!')

if len(numeros[1]) > 0:
    print(f'Os valores PARES digitados foram {sorted(numeros[1])}!')
else:
    print('Não foi digitado nenhum valor PAR!')

if len(numeros[0]) == 0 and len(numeros[1]) == 0:
    print('Foram digitados apenas valores NEUTROS!')