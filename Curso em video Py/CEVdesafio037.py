from time import sleep

decimal = int(input('Escolha um numero inteiro : '))
print('\033[33mEscolha uma das bases de conversão')
sleep(1)
print('\033[34m[1] BINÁRIO\n[2] OCTAL\n[3] HEXADECIMAL')
sleep(1)
escolha = int(input('\033[mSua opção : '))
sleep(1)

if escolha == 1:
    binario = bin(decimal)
    print('O numero \033[4;32m{}\033[m convertido para Binário é igual a \033[4;32m{}\033[m'.format(decimal, binario[2:]))
elif escolha == 2:
    octal = oct(decimal)
    print('O numero \033[4;32m{}\033[m convertido para Octal é igual a \033[4;32m{}\033[m'.format(decimal, octal[2:]))
elif escolha == 3:
    hexadecimal = hex(decimal)
    print('O numero \033[4;32m{}\033[m convertido para Hexadecimal é igual a \033[4;32m{}\033[m'.format(decimal, hexadecimal[2:]))
else:
    print('Essa não é uma opção válida!!')