n, soma, cont = 0, 0, 0

while n < 999:
    n = int(input('Digite um numero [digite 999 para parar] : '))

    if n < 999:
        soma += n
        cont += 1

print('Você digitou {} numeros e a soma entre eles resulta em {}'.format(cont, soma))
