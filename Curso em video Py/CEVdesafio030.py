numero = int(input('Digite um numero qualquer : '))
parimpar = numero % 2

if parimpar == 1:
    print('O numero que você digitou foi \033[4;35m{}\033[m e ele é um numero \033[36mÍMPAR\033[m!'.format(numero))
else:
    print('O numero que você digitou foi \033[4;32m{}\033[m e ele é um numero \033[36mPAR\033[m!'.format(numero))