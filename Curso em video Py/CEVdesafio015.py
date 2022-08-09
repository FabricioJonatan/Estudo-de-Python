dias = int(input('Quantos dias esse carro foi alugado : '))
km = float(input('Quantos km foram percorridos por este carro : '))
preço = (dias * 60) + (km * 0.15)

print('O total a pagar é {:.2f}R$'.format(preço))