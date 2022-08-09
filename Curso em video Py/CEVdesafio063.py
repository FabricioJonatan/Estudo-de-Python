print('+=' * 20)
print('        Sequencia de Fibonacci')
print('+=' * 20)

termos = int(input('Quantos termos deseja imprimir? '))
cont = 3
na = 0
n = 1
nat = n + na

print('{} -> {} -> '.format(na, n), end = '')

while cont <= termos:
    print('{} -> '.format(nat), end = '')

    na = n
    n = nat
    nat = na + n
    cont += 1

print('FIM')
print('~' * 40)
