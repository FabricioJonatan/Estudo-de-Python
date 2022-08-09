from datetime import date

nascimento = int(input('Ano em que você nasceu : '))
ano = date.today().year
idade = ano - nascimento
alistamento = nascimento + 18

print('Quem nasceu em {} faz {} anos em {}'.format(nascimento, idade, ano))

if idade > 18:
    saldo = idade - 18
    print('Você já devia ter se alistado há {} anos atrás!'.format(saldo))
    print('Seu alistamento foi em {}'.format(alistamento))
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o seu alistamento!'.format(saldo))
    print('Seu alistamento será em {}'.format(alistamento))
else:
    print('\033[31mVOCÊ TEM QUE SE ALISTAR IMEDIATAMENTE!!\033[m')