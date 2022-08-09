from random import randint

print('\033[35m=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('\033[36mEu irei pensar em um numero de 1 a 5, tente adivinhar!!')
print('\033[35m=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

numeroR = randint(1, 5)
numeroS = int(input('\033[33mEm que numero pensei?  '))

if numeroR == numeroS:
    print('\033[32mParabens! Você acertou!!!')
elif numeroR != numeroS:
    print('\033[31mQue pena, você errou!')