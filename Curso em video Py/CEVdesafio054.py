from datetime import date
pessoas = int(input('Quantas pessoas deseja informar? '))

maior = 0
menor = 0

for c in range(1, pessoas + 1):
    ano = int(input('Em que ano a {}° pessoa nasceu? '.format(c)))
    anoatual = date.today().year

    if anoatual - ano >= 18:
        maior += 1
    else:
        menor += 1

print('Ao todo tem {} pessoas maiores de idade'.format(maior))
print('E {} pessoas menores de idade!'.format(menor))