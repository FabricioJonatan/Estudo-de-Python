from random import randint

numeros = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))

for i in range(len(numeros)):
    if i == 0:
        maior = menor = numeros[i]
    else:
        if maior < numeros[i]:
            maior = numeros[i]
        if menor > numeros[i]:
            menor = numeros[i]

print('Os valores sorteados foram : ', end = '')

for num in numeros:
    print(f'\033[36m{num} \033[m', end = '')

print(f'\nO \033[32mmaior\033[m numero sorteado foi \033[32m{maior}\033[m')
print(f'O \033[31mmenor\033[m numero sorteado foi \033[31m{menor}\033[m')
