print('\033[33mPARA ENCERRAR O PROGRAMA DIGITE UM NUMERO NEGATIVO\033[m')
print('=' * 30)
tabuada = int(input('Digite um numero da sua tabuada : '))
print('=' * 30)

while True:

    if tabuada < 0:
        break

    for numero in range(1, 11):
        resultado = numero * tabuada
        print(f'{tabuada} X {numero} = {resultado}')
        numero += 1

    print('=' * 30)
    tabuada = int(input('Digite um numero da sua tabuada : '))
    print('=' * 30)

print('PROGRAMA DE TABUADA ENCERRADO, Volte sempre!!')