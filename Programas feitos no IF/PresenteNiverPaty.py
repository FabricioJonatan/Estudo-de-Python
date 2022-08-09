idade = int(input('Qual a sua idade? '))

if idade < 18:
    print('Hmmm então você é mais novo(a) que o amor da minha vida.')
    print('Então você não tem essa semelhança com a coisinha mais \n perfeita do mundo atualmente maior de idade sinto pena')

elif idade > 18:
    print('Uou tu é mais velho(a) do que a pessoa que mais amo do mundo.')
    print('Deve ser difícil lidar com as responsabilidades de seer adulto né\nO meu amorzinho dar conta disso de boa chega a ser impressionante')
    print('Ela nem era adulta e já dava inveja em um monte de gente com o quão desenrolada e incrivel ela é!')

else:
    print('Você deve ser bem feliz por ter essa semelhança com a melhor pessoa do mundo cara sério aaaaah')
    print('Sabia que hoje é um dia mega especial pra pessoa mais especial \ndo mundo a qual eu amo mais do que minha mãe com certeza ksks?')

while True:
    resposta = input('Você deseja falar da idade de mais alguém? [S / N] ').strip().lower()

    if resposta == 'n':
        break
    elif resposta == 's':
        idade = int(input('Qual a idade dessa pessoa? '))

        if idade < 18:
            print('Hmmm então essa pessoa é mais novo(a) que o amor da minha vida.')
            print('Então ela não tem essa semelhança com a coisinha mais \n perfeita do mundo, atualmente maior de idade sinto pena')

        elif idade > 18:
            print('Uou essa pessoa é mais velha do que a pessoa que mais amo do mundo.')
            print('''Deve ser difícil lidar com as responsabilidades de seer adulto né
            O meu amorzinho consegue dar conta disso de boa, chega a ser impressionante''')
            print('Ela nem era adulta e já dava inveja em um monte de gente com o quão desenrolada e incrivel ela é!')

        else:
            print('Esta pessoa deve ser bem feliz por ter essa semelhança com a melhor pessoa do mundo cara sério aaaaah')
            print('Sabia que hoje é um dia mega especial pra pessoa mais especial \ndo mundo a qual eu amo mais do que minha mãe com certeza ksks?')

    else:
        print('Resposta inválida, responda novamente!')

amor = int(input('Se você ama alguém, seja familiar ou algo assim, em uma escala de 0 a 10 quanto você ama essa pessoa? '))

if amor < 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999:
    print('''Isso que tu chama de amor? patético muahahaha, a pessoa que amo é tão incrivel
    que se recebesse só isso de amor com certeza iria descobrir uma forma de mexer com o espaço tempo e
    multiplicar isso cara, e no processo ainda iria encher todos de orgulho por ser tão foda!!''')
    
else:
    print('Parabéns, você tem 1 terço do meu amor por Patricia de Lima Rodriguez!')