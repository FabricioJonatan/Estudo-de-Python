from random import randint
from time import sleep

itens = ('PEDRA', 'PAPEL', 'TESOURA')
adversario = randint(0, 2)

print('''Suas opções são :
\033[4m[0] PEDRA
[1] PAPEL
[2] TESOURA\033[m''')

jogador = int(input('Qual a sua escolha? '))

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('POH!!')
print('\033[35m', '=' * 30, '\033[m')
print('  O computador jogou : \033[1;34m{}\033[m'.format(itens[adversario]))
print('  E você jogou : \033[1;36m{}\033[m'.format(itens[jogador]))
print('\033[35m', '=' * 30, '\033[m')

if adversario == 0:
    if jogador == 0:
        print('\033[31mEMPATOU\033[m')
    elif jogador == 1:
        print('\033[32mVocê ganhou!!\033[m')
    else:
        print('\033[31mVocê perdeu!\033[m')
elif adversario == 1:
    if jogador == 0:
        print('\033[31mVocê perdeu!\033[m')
    elif jogador == 1:
        print('\033[33mEMPATOU\033[m')
    else:
        print('\033[32mVocê ganhou!!\033[m')
else:
    if jogador == 0:
        print('\033[32mVocê ganhou!!\033[m')
    elif jogador == 1:
        print('\033[31mVocê perdeu!\033[m')
    else:
        print('\033[33mEMPATOU\033[m')