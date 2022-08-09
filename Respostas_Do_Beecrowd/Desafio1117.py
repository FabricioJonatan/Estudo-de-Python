soma, cont = 0, 0

while True:
    nota = float(input())

    if nota >= 0 and nota <= 10:
        soma += nota
        cont += 1
    else:
        print('nota invalida')
    
    if cont == 2:
        break

media = soma / cont
print('media = {}'.format(media))