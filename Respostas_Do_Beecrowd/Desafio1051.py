renda = float(input())

if renda <= 2000:
    print('Isento')

elif renda <= 3000:
    renda -= 2000
    imposto = renda * 8 / 100
    print('R$ {:.2f}'.format(imposto))

elif renda <= 4500:
    renda -= 1000 + 2000
    imposto = (1000 * 8 / 100) + (renda * 18 / 100)
    print('R$ {:.2f}'.format(imposto))

else:
    renda -= 4500
    imposto = (1000 * 8 / 100) + (1500 * 18 / 100) + (renda * 28 / 100)
    print('R$ {:.2f}'.format(imposto))