altura = float(input('Qual a altura da parede : '))
largura = float(input('Qual a largura da parede : '))
area = altura * largura
tinta = area / 2

print('As prorpoções da parede são {} x {} e sua área é de {} m²'.format(altura, largura, area))
print('Para pintar esta parede será necesario {} L de tinta'.format(tinta))