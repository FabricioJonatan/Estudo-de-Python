numero1 = int(input('Primeiro numero : '))
numero2 = int(input('Segundo numero : '))

if numero1 > numero2:
    print('O \033[1;35mPrimeiro\033[m valor é o maior!')
elif numero2 > numero1:
    print('O \033[1;36mSegundo\033[m valor é o maior!')
else:
    print('Os dois valores são \033[1;34mIguais\033[m!')