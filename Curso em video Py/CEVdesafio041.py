from datetime import date
def categoria(a):
    print(f'\033[4;34ma categoria deste nadador é \033[1;36m{a}\033[m')

nascimento = int(input('Qual o ano de nascimento deste nadador? '))
idade = date.today().year - nascimento
print(f'\033[4mA idade deste Nadador é de \033[36m{idade} anos\033[4;39m, logo\033[m')

if idade <= 9:
    categoria('MIRIM')
elif idade <= 14:
    categoria('INFANTIL')
elif idade <= 19:
    categoria('JUNIOR')
elif idade <= 25:
    categoria('SÊNIOR')
else:
    categoria('MASTER')