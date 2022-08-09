from random import randint

print('-=' * 20)
print('       VAMOS JOGAR PAR OU IMPAR')
print('-=' * 20)

while True:
    valorpc = randint(0, 20)
    valor = int(input('Digite o seu numero : '))
    resultado = valor + valorpc
    escolha = 'a'

    while escolha not in 'pi':
        escolha = input('Você de seja impar ou par? [I/P] ').lower().strip()

    parim = 'PAR' if resultado % 2 == 0 else 'IMPAR'
        
    print('--' * 20)
    print(f'Você jogou {valor} e o computador jogou {valorpc} e o total deu {resultado} que é {parim}\n')

    if resultado % 2 == 0:
        if escolha == 'i':
            print('Você PERDEU!')
            break
        else:
            print('Você VENCEU!!')
            print('Vamos jogar de novo . . .')

    else:
        if escolha == 'p':
            print('Você PERDEU!')
            break
        else:
            print('Você VENCEU!!')
            print('Vamos jogar de novo . . .')
        