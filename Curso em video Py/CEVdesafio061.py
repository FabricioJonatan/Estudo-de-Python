print('=' * 23)
print(' 10 TERMOS DE UMA "PA"')
print('=' * 23)

termo = int(input('Primeiro termo : '))
razao = int(input('Razão : '))
final = razao * 10 + termo

while termo < final:
    print(f'{termo} -> ', end = '')
    termo += razao

print('FIM!')