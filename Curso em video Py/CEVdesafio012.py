preço = float(input('Qual o preço do produto? R$'))
desconto = preço * 5 / 100
preçonovo = preço - desconto

print('O produto que custava {}R$, na promoção de 5%, passou a custar {}R$'.format(preço, preçonovo))