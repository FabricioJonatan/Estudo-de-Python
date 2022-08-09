extenso = ('zero', 'um', 'dois', 'três', 'quatro', 
'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
'doze', 'treze', 'quartoze', 'quinze', 'dezesseis', 'dezessete',
'dezoito', 'dezenove', 'vinte')

numero =  int(input('Digite um numero de 0 a 20 : '))

while True:
    if numero in range(len(extenso)):
        print(f'Você digitou o numero \033[36m{extenso[numero]}\033[m')
        break
    else:
        numero =  int(input('Tente novamente. Digite um numero de 0 a 20 : '))