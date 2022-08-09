from time import sleep

decimal = int(input('Digite o numero decimal que deseja converter : '))
numero = decimal

while True:
    n1 = decimal % 2
    decimal = decimal // 2
    n2 = decimal % 2
    decimal = decimal // 2
    n3 = decimal % 2
    decimal = decimal // 2
    n4 = decimal % 2
    decimal = decimal // 2
    n5 = decimal % 2
    decimal = decimal // 2
    n6 = decimal % 2
    decimal = decimal // 2
    n7 = decimal % 2
    n8 = decimal // 2

    n1, n2, n3, n4, n5, n6, n7, n8 = int(n1), int(n2), int(n3), int(n4), int(n5), int(n6), int(n7), int(n8)
    
    print('Analisando numero . . .')
    sleep(1)
    print('O numero {} fica \033[32m{} {} {} {} {} {} {} {}\033[39m em BINÁRIO'.format(numero, n8, n7, n6, n5, n4, n3, n2, n1))
    resposta = int(input('Deseja converter outro numero?\n \033[32m 1 : SIM  \033[31m 2 : NÂO \n\033[39m  '))
    if resposta == 1:
        print('Preparando sistema . . .')
        sleep(1)
        decimal = int(input('Digite o numero decimal que deseja converter : '))
        numero = decimal
    else:
        print('Até a próxima!!')
        break