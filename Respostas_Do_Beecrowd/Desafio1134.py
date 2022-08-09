gas, dis, alc = 0, 0, 0

while True:
    combustivel = int(input())

    if combustivel == 1:
        alc += 1
    if combustivel == 2:
        gas += 1
    if combustivel == 3:
        dis += 1
    if combustivel == 4:
        break

print('MUITO OBRIGADO')
print('Alcool: {}'.format(alc))
print('Gasolina: {}'.format(gas))
print('Diesel: {}'.format(dis))