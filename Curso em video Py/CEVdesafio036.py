casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o salario mensal do comprador? '))
anos = int(input('Em quantos anos deseja ter essa casa? '))
prestação = casa / (anos * 12)
porcentagem = (salario * 30) / 100

print('\nPara pagar uma casa de \033[4;32m{:.2f}\033[m em \033[4;32m{}\033[m ano(s)'.format(casa, anos))
print('A prestação será de \033[4;32m{:.2f}\033[m'.format(prestação))

if porcentagem <= prestação:
    print('\033[31mSeu financiamento foi REJEITADO por não atender os requisitos minimos!\033[m')
else:
    print('\033[32mSeu financiamento foi CONCEBIDO\033[m')