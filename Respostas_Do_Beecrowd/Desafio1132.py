x = int(input())
y = int(input())
soma = 0

maior = x if x > y else y
menor = x if x < y else y

for c in range(menor, maior + 1):
    if c % 13 != 0:
        soma += c

print(soma)