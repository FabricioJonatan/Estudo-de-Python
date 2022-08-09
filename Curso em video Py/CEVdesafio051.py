print('=' * 23)
print(' 10 TERMOS DE UMA "PA"')
print('=' * 23)

termo = int(input('Primeiro termo : '))
razao = int(input('Razão : '))
final = razao * 10 + termo

for c in range(termo, final, razao):
    print(f'{c} -> ', end = '')

print('FIM!')