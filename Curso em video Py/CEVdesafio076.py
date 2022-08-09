listagem = ('Caderno', 23, 'Lapis', 0.7, 'Caneta', 1,
'Lapiseira', 1.5, 'Cartulina', 0.3, 'Borracha', 0.5)

print('=' * 40)
print(f'{"LISTAGEM DE PREÇOS" :^40}')
print('=' * 40)

for pos in range(len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end = '')
    else:
        print(f'R$ {listagem[pos]:>5.2f}')
        
print('=' * 40)