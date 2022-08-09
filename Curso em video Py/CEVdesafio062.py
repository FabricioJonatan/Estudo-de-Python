print('=' * 23)
print(' 10 TERMOS DE UMA "PA"')
print('=' * 23)

primeiro = int(input('Primeiro termo : '))
razao = int(input('Razão : '))
cont = 1
total = 0
add = 10

while add != 0:
    total += add
    while cont <= total:
        print(f'{primeiro} -> ', end = '')
        primeiro += razao
        cont += 1

    print('PAUSA')
    add = int(input('Quantos termos você quer mostrar a mais? '))

print(f'\nProgressão finalizada com {total} termos mostrados!!')