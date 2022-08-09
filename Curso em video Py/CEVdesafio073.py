from gettext import find


times = ('Corinthians', 'Atlético Mineiro', 'Flamengo', 'Red Bull Bragantino', 'Santos',
'Fluminense', 'São Paulo', 'América FC', 'Coritiba', 'Botafogo', 'Cuiaba Esporte Clube', 'Ceará',
'Internacional', 'Avaí', 'Palmeiras', 'Juventude', 'Goiás', 'Atlético Goianiense', 'Fortaleza', 'Atlético Paranaense')

print('\n', '{:^40}'.format('~~~~BRASILEIRÃO 2021~~~~'))
print('==' * 19)
print('{:^40}'.format('Primeiros 5 Colocados :'))
print('==' * 19, '\n')

for colocados in range(5):
    print(f'{colocados + 1}° colocado : {times[colocados]}')

print('\n', '==' * 19)
print('{:^40}'.format('Ultimos 4 colocados :'))
print('==' * 19, '\n')

for ultimos in range(len(times) - 4, len(times)):
    print(f'{ultimos + 1}° colocado : {times[ultimos]}')

print('\n', '==' * 19)
print('{:^40}'.format('todos os times em ordem A - Z :'))
print('==' * 19, '\n')
print(sorted(times))

print('\nO time favorito da minha familia (Fortaleza) se encontra em {}° lugar'.format(times.index('Fortaleza') + 1))