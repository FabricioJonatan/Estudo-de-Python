soma = 0
impar = 0

for c in range(1, 7):
    numero = int(input('Digite um valor : '))
    if numero % 2 == 0:
        soma += numero
    else:
        impar += 1

print(f'A soma dos numeros pares digitados dá : \033[35m{soma}\033[m')
print(f'Foram digitados \033[34m{impar}\033[m numeros impares')