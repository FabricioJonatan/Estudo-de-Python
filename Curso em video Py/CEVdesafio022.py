from time import sleep

nome = input('Digite seu nome completo : ').strip()

sleep(1)
print('Analisando seu nome aguarde . . .')
sleep(1)

print('Seu nome com todas as letras em maiusculas é {}'.format(nome.upper()))
print('Seu nome com todas as letras em minusculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeito nome possui {} letras'.format(nome.find(' ')))