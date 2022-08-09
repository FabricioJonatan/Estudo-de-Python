pessoa = {}

pessoa['nome'] = input('Nome : ').capitalize().strip()
nascimento = int(input('Data de nascimento : '))
pessoa['idade'] = 2022 - nascimento
pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem) : '))

if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de Contratação : '))
    pessoa['salario'] = float(input('Salário : '))
    pessoa['aposentadoria'] = pessoa['idade'] + pessoa['contratação'] + 35 - 2022

for key, valor in pessoa.items():
    print(f'   -   O valor {key} tem {valor}')