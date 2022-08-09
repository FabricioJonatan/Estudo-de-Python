from time import sleep

a = int(input('Digite o primeiro valor : '))
b = int(input('Digite o segundo valor : '))
sleep(1)

print('''
[ 1 ] Somar valores
[ 2 ] Multiplicar valores
[ 3 ] Maior dos valores
[ 4 ] Novos valores
[ 5 ] Fechar o programa
''')

escolha = int(input('>>>>> Sua escolha : '))
sleep(1)

while True:
    if escolha == 1:
        soma = a + b
        print(f'\nA soma de {a} mais {b} resultam em {soma}')
        print('=' * 30)

    elif escolha == 2:
        multi = a * b
        print(f'\nA multiplicação de {a} mais {b} resulta em {multi}')
        print('=' * 30)

    elif escolha == 3:
        if a > b:
            maior = a
        else:
            maior = b
        print(f'\nEntre {a} e {b} o maior valor é {maior}')
    
    elif escolha == 4:
        a = int(input('Digite o primeiro valor : '))
        b = int(input('Digite o segundo valor : '))
        sleep(1)
        print('Novos valores salvos. . .')

    elif escolha == 5:
        print('Até uma próxima!!\nFechando progama . . .')
        sleep(1)
        break
    else:
        print('Opção inválida! Tente novamente!!')

    sleep(2)
    print('''
[ 1 ] Somar valores
[ 2 ] Multiplicar valores
[ 3 ] Maior dos valores
[ 4 ] Novos valores
[ 5 ] Fechar o programa
''')

    escolha = int(input('>>>>> Sua escolha : '))
    sleep(1)

print('PROGRAMA FECHADO COM SUCESSO!!!')