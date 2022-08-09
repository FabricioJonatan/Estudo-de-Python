a = int(input('Digite o Primeiro numero : '))
b = int(input('Digite o Segundo numero : '))
c = int(input('Digite o Terceiro numero : '))

if a >= b and a >= c:
    maior = a
if b >= a and b >= c:
    maior = b
if c >= a and c >= b:
    maior = c

if a <= b and a <= c:
    menor = a
if b <= a and b <= c:
    menor = b
if c <= a and c <= b:
    menor = c

print('\033[4;39m O Maior numero digitado \033[2;32m{}\033[;39m'.format(maior))
print('\033[4;39m O Menor numero digitado \033[2;32m{}\033[;39m'.format(menor))