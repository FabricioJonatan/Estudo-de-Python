pessoas = []
posição = 0

while True:
    nome = input('Nome : ').strip().capitalize()
    peso = float(input('Peso : '))
    pessoa = [nome, peso]
    pessoas.append(pessoa)

    while True:
        resposta = input('Deseja continuar? [S/N] ').lower().strip()
        if resposta in 'sn': break
        else: print('Resposta inválida, digite novamete!')

    if resposta == 'n': break

for pessoa in pessoas:
    if posição == 0:
        maior = pessoas[posição][1]
        menor = pessoas[posição][1]
    else:
        if pessoas[posição][1] > maior:
            maior = pessoas[posição][1]
        if pessoas[posição][1] < menor:
            menor = pessoas[posição][1]
    posição += 1
posição = 0

print('=-' * 15)
print(f'Ao todo você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior:.2f} KG. Peso pertencente ', end = '')
for pessoa in pessoas:
    if pessoas[posição][1] == maior:
        print(f'[{pessoas[posição][0]}] ', end = '')
    posição += 1
posição = 0
        
print(f'\nO menor peso foi de {menor:.2f} KG. Peso pertencente ', end = '')
for pessoa in pessoas:
    if pessoas[posição][1] == menor:
        print(f'[{pessoas[posição][0]}] ', end = '')
    posição += 1