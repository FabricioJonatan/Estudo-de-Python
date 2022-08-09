pessoas = int(input('Quantas pessoas deseja cadastrar? '))

for c in range(1, pessoas + 1):
    print('=' * 7, '{} PESSOA')
    nome = input('NOME : ')
    idade = input('IDADE : ')
    sexo = input('SEXO [M/F] : ')
