soma, cont, escolha = 0, 0, 0

while True:
    nota = float(input())

    if nota >= 0 and nota <= 10:
        soma += nota
        cont += 1
    else:
        print('nota invalida')
    
    if cont == 2:
        media = soma / cont
        print('media = {:.2f}'.format(media))
        soma, cont, escolha = 0, 0, 0

        while True:
            print('novo calculo (1-sim 2-nao)')
            escolha = int(input())

            if escolha == 1:
                break
            if escolha == 2:
                break
    if escolha == 2:
        break
