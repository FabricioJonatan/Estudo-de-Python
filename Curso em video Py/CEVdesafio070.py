print('¨-¨=' * 10)
print('\033[35m           LOJINHO DO TADEU\033[m')
print('¨-¨=' * 10)

total = mais1000 = quant = 0

while True:
    produto = input('Nome do produto : ').strip().capitalize()
    preço = float(input('Preço : R$ '))
    quant += 1
    total += preço
    
    if preço >= 1000:
        mais1000 += 1
    if quant == 1 or preço < menor:
        menor = preço
        menornome = produto

    while True:
        escolha = input('Deseja continuar? [S/N]').strip().lower()

        if escolha == 'n' or escolha == 's':
            break
        else:
            print('Opção invalida!')
    if escolha == 'n':
        break

print(f'''
=-=-=-=-= FIM DO PROGRAMA =-=-=-=-=-

O total da compra foi R$ {total:.2f}
Temos {mais1000} produto(s) custando mais de R$ 1.000
O produto mais barato foi um(a) {menornome} que custou R$ {menor:.2f}
''')
