numero = int(input())

for c in range(1, numero + 1):
    if c % 2 == 0:
        quadrado = c ** 2
        print('{}^2 = {}'.format(c, quadrado))