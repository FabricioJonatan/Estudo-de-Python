from datetime import date

ano = int(input('Que ano você gostaria de analisar?(pressione 0 se quiser analisar o ano atual) : '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {}{} é Bissexto{}!'.format('\033[4;32m', ano, '\033[m'))
else:
    print('O ano de {}{} não é Bissexto{}!'.format('\033[4;31m', ano, '\033[m'))