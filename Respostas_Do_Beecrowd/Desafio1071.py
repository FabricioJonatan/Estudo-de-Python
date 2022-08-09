x = int(input())
y = int(input())
soma = 0

if x > y:
    maior = x
else:
    maior = y
if y < x:
    menor = y
else:
    menor = x

for c in range(menor + 1, maior):
    if c % 2 == 1:
        soma += c

print(soma)