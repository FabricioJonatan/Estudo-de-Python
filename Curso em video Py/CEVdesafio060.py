fatorial = int(input('Digite o numero que deseja ver seu fatorial : '))
numero = fatorial
multi = 1

print(f'\nO fatorial de {fatorial} = ', end = '')
while numero > 0:
    print(f'{numero}', end = '')
    print(' x ' if numero > 1 else ' = ', end = '')

    multi *= numero
    numero -= 1

print(multi)