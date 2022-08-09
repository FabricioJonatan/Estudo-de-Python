salario = float(input('Qual o salario deste funcionário : R$'))
aumento = salario * 15 / 100
novosalario = aumento + salario

print('O funcionário que recebia {} R$ com um aumento de 15% passará a receber {:.2f} R$'.format(salario, novosalario))