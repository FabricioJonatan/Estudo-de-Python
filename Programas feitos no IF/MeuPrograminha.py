a = input('1 : Cadastrar \n2 : Listar \n3 : Mostrar dados salvos \n0 : Sair \nDigite um numero \n')
nome = '(NÃO CADASTRADO)'
numero = '(NÃO CADASTRADO)'
a1 = '(xx)x xxxx-xxxx'
a2 = '(xx)x xxxx-xxxx'
a3 = '(xx)x xxxx-xxxx'

from time import sleep

while a != '0': 
    if a == '1':
        nome = input('Nome :')
        numero = input('Numero :')
        sleep(1)
        print('Seu nome é {} e seu numero é {}'.format(nome, numero))
        sleep(1)
        print('Dados salvos!')
        sleep(1)
    elif a == '2':
        num = input('Quantos numeros você deseja adicionar a lista? (max 3) :')
        sleep(1)
        if num == '3':
            a1 = input('Numero 1 :')
            a2 = input('Numero 2 :')
            a3 = input('Numero 3 :')
            sleep(1)
            print('Numeros salvos!')
            sleep(1)
            
        elif num == '2':
            a1 = input('Numero 1 :')
            a2 = input('Numero 2 :')
            sleep(1)
            print('Numeros salvos!')
            sleep(1)
        elif num == '1':
            a1 = input('Numero 1 :')
            sleep(1)
            print('Numeros salvos!')
            sleep(1)
        else:
            print('Este não é um numero válido ou não é um numero\ndigite novamente!')
            sleep(1)
    elif a == '3':
        print('Seu nome é : {}\nSeu numero é : {}'.format(nome, numero))
        sleep(3)
        print('Seus numeros salvos são :')
        sleep(1)
        print('Numero 1 : {}'.format(a1))
        sleep(1)
        print('Numero 2 : {}'.format(a2))
        sleep(1)
        print('Numero 3 : {}'.format(a3))
        sleep(5)
        if nome == '(NÃO CADASTRADO)' and numero == '(NÃO CADASTRADO)':
            print('Notamos que não está cadastrado, pedimos que se cadastre para conseguir\nconsultar todos os seus dados sempre que quiser ')
            sleep(3)
        if a1 == '(xx)x xxxx-xxxx':
            print('Notamos que você não possui numeros salvos\nrecomendamos que salve seus numeros para ter acesso a eles futuramente')
            sleep(3)
    else:
        print('Isso não é uma opção válida, digite novamente!')
        sleep(1)
    a = input('1 : Cadastrar \n2 : Listar \n3 : Mostrar dados salvos \n0 : Sair \nDigite um numero \n')