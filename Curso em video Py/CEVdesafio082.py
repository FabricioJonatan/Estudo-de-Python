lista = []
pares = []
impares = []

while True:
    numero = int(input('Digite um número qualquer : '))
    lista.append(numero)

    while True:
        resposta = input('Deseja digitar outro número? [S/N] ').strip().lower()

        if resposta in 'sn':  break
        else: print('Resposta inválida, digite novmente por favor.')

    if resposta == 'n': break

for numeros in lista:
    if numeros % 2 == 0:
        pares.append(numeros)
    else:
        impares.append(numeros)

print('~~~~' * 20)
print(f'A lista completa digitada em ordem é {sorted(lista)}')
print(f'A lista de números pares em ordem é {sorted(pares)}')
print(f'A lista de números ímpares em ordem é {sorted(impares)}')