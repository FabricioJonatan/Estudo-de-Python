salario = float(input())

if salario <= 400:
    reajuste = salario * 15 / 100
    nsal = salario + reajuste
    porcento = 15
    
elif salario <= 800:
    reajuste = salario * 12 / 100
    nsal = salario + reajuste
    porcento = 12

elif salario <= 1200:
    reajuste = salario * 10 / 100
    nsal = salario + reajuste
    porcento = 10

elif salario <= 2000:
    reajuste = salario * 7 / 100
    nsal = salario + reajuste
    porcento = 7

else:
    reajuste = salario * 4 / 100
    nsal = salario + reajuste
    porcento = 4

print('Novo salario: {:.2f}'.format(nsal))
print('Reajuste ganho: {:.2f}'.format(reajuste))
print('Em percentual: {} %'.format(porcento))