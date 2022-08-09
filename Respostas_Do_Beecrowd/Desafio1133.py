x = int(input())
y = int(input())

maior = x if x > y else y
menor = x if x < y else y

for c in range(menor + 1, maior):
    if c % 5 == 2 or c % 5 == 3:
        print(c)