pessoa = {}
pessoa['nome'] = input('Nome: ').capitalize().strip()
pessoa['media'] = float(input(f'Média de {pessoa["nome"]} : '))

if pessoa['media'] >= 7:
    pessoa['situação'] = 'aprovado(a)'
elif pessoa['media'] >= 5:
    pessoa['situação'] = 'recuperação'
else:
    pessoa['situação'] = 'reprovado(a)'

print('~=' * 15)
for key, valor in pessoa.items():
    print(f'   - {key} é igual a {valor}')