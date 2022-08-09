numero = int(input('Digite um numero inteiro : '))
diviseis = 0

print('=' * 35)

for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[34m', end = '')
        diviseis += 1
    else:
        print('\033[33m', end = '')

    print(f'{c}\033[m, ', end = '')

print('FIM\n')
print(f'O numero \033[36m{numero}\033[m foi divisivel por \033[36m{diviseis}\033[m numeros')

if diviseis == 2:
    print('Por isso ele \033[32mÉ\033[m um numero primo!!\n')
else:
    print('Por isso ele \033[31mNÃO\033[m é um numero primo!!\n')