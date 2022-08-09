continuar, contador, maior, homens, mulhermaior = 's', 0, 0, 0, 0

while continuar not in 'n':
    contador += 1

    print('==' * 20)
    print('      Cadastre a {}° pessoa'.format(contador))
    print('==' * 20)

    idade = int(input('Idade : '))

    while True:
        sexo = input('Sexo [H/M] : ').strip().upper()
        if sexo == 'H' or sexo == 'M':
            break
        else:
            print('Opção invalida!')


    if idade >= 18:
        maior += 1
    if sexo == 'H':
        homens += 1
    if sexo == 'M' and idade < 20:
        mulhermaior += 1
    
    while True:
        escolha = input('Quer continuar? [S/N] ').strip().upper()
        if escolha == 'N' or escolha == 'S':
            break
        else:
            print('Opção inválida!')

    if escolha == 'N':
        break

print(f'''
Total de pessoas com mais de 18 anos são/é {maior}
Ao todo temos {homens} homen(s) cadastrado
E temos {mulhermaior} mulher(es) com menos de 20 anos''')