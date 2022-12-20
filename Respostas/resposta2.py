conta = 1
positivo = contador = negativo = 0
contas = []

while True:
    conta_num = int(input('Digite o número da conta [digite 0 ou número negativo para sair]: '))
    if conta_num <= 0:
        break

    saldo = int(input('Digite o saldo desta conta : '))

    if saldo > 0:
        positivo += 1
    else:
        negativo += 1
    contador += 1

    conta = [conta_num, saldo]
    contas.append(conta)

porcentagem = (negativo / contador) * 100
print(f'\n\nContas informadas {contas}')
print(f'Total de saldos negativos : {porcentagem:.2f}%')