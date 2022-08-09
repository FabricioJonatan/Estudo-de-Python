from time import sleep

numero = int(input('Digite um numero de 1 a 9999 : '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

sleep(1)
print('Analisando o número . . .')
sleep(1)

print('Unidade : {}'.format(u))
print('Dezena : {}'.format(d))
print('Cetena : {}'.format(c))
print('Milhar : {}'.format(m))