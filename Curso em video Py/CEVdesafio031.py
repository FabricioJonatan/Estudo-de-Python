distancia = float(input('Qual a distância da viagem que desesjas fazer? '))

if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('Você esta prestes a começar uma viagem de {:.2f} Km'.format(distancia))
print('O preço de sua viagem será de {:.2f} R$'.format(preço))