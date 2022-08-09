valores = []

for cont in range(5):
    valores.append(int(input(f'Digite o valor para a posição {cont} : ')))

    if cont == 0:
        menor = maior = valores[cont] 
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]

print(f'Os numeros digitados foram : {valores}')
print(f'O maior valor lido foi {maior} nas posições ', end = '')

for pos, valor in enumerate(valores):
    if valor == maior:
        print(f'{pos}... ')

print(f'O menor valor lido foi {menor} nas posições ', end = '')

for pos, valor in enumerate(valores):
    if valor == menor:
        print(f'{pos}... ')
