def status(gordo):
    print(f'\033[1;32m{gordo}\033[m')


peso = float(input('Digite o peso de uma pessoa : '))
altura = float(input('Digite a altura de uma pessoa : '))
imc = peso / (altura ** 2)

print(f'O IMC desta pessoa é de {imc:.2f} logo essa pessoa está : ', end = (''))

if imc <= 18.5:
    status('ABAIXO DO PESO!')
elif imc <= 25:
    status('NO PESO IDEAL!')
elif imc <= 30:
    status('COM SOBREPESO!')
elif imc <= 40:
    status('OBESO!')
else:
    status('COM OBESIDADE MÓRBIDA! Tome cuidado!')