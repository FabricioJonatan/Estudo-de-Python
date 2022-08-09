from random import randint

print('\033[35m=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('\033[36mEu irei pensar em um numero de 1 a 10, tente adivinhar!!')
print('\033[35m=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('\033[mATENÇÂO! O jogo só encerrara quando você acertar.\n')

numeroS = int(input('\033[33mEm que numero pensei?  '))
numeroR = randint(1, 10)

if numeroR == numeroS:
    print('\033[32mParabens! Você acertou!!!\033[m')
elif numeroR != numeroS:
    print('\033[31mQue pena, você errou!\033[m')

while numeroR != numeroS:
    print('Tente novamente!!')

    numeroS = int(input('\033[33mEm que numero pensei?  '))
    numeroR = randint(1, 10)

    if numeroR == numeroS:
        print('\033[32mParabens! Você acertou!!!\033[m')
    elif numeroR != numeroS:
        print('\033[31mQue pena, você errou!\033[m')
