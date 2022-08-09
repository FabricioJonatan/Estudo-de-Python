def textpre():
    print(f'Sua compra de \033[32m{preço:.2f}\033[m R$ vai custar \033[32m{total:.2f}\033[m R$ no final!')


print('=' * 10, '\033[1;35mLOJINHA DO TADEU\033[m', '=' * 10)

preço = float(input('\033[4mPreço das compras \033[m: '))

print('[1] á vista dinheiro/cheque\n[2] á vista cartão\n[3] 2x no cartão\n[4] 3x ou mais vezes no cartão')

resposta = input('\033[4mQual sua escolha \033[m: ')

if resposta == '1':
    total = preço - (preço * 10 / 100)
    textpre()
elif resposta == '2':
    total = preço - (preço * 5 / 100)
    textpre()
elif resposta == '3':
    parcelas = preço / 2
    total = preço
    print(f'Sua compra ficará de 2x de {parcelas:.2f} R$')
    textpre()
else:
    parcela = int(input('Quantas parcelas deseja? '))
    parcelas = preço / parcela
    total = preço + (preço * 20 / 100)
    print(f'Sua compra ficará de {parcela}x de {parcelas:.2f} R$')
    textpre()
