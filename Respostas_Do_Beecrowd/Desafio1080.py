for c in range(1, 101):
    n = int(input())

    if c == 1:
        maior = n
    else:
        if n > maior:
            maior = n
            posicao = c

print(maior)
print(posicao)