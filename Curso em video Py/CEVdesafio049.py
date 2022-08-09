tabuada = int(input('Digite um numero da sua tabuada : '))

print('=' * 13)

for numero in range(1, 11):
    resultado = numero * tabuada
    print(f'{tabuada} X {numero} = {resultado}')
    numero += 1

print('=' * 13)