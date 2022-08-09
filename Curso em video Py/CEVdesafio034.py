salario = float(input('Qual o salário deste funcionário? R$ '))

if salario >= 1250:
    aumento = salario + (salario * 10 / 100)
else:
    aumento = salario + (salario * 15 / 100)

print('Quem ganhava \033[4;32m{:.2f} R$\033[0;39m, agora ganhará \033[4;32m{:.2f} R$\033[0;39m'.format(salario, aumento))