matriz = []
somapar = 0

        # PROGRAMA PRINCIPAL : 

for linha in range(3):
    valor1 = int(input(f'Digite o valor para [{linha}, 0] : '))
    valor2 = int(input(f'Digite o valor para [{linha}, 1] : '))
    valor3 = int(input(f'Digite o valor para [{linha}, 2] : '))
    line = [valor1, valor2, valor3]
    matriz.append(line)

for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]

for c in range(len(matriz[1])):
    if c == 0:
        maior = matriz[1][c]
    else:
        if maior < matriz[1][c]:
            maior = matriz[1][c]

soma = matriz[0][2] + matriz[1][2] + matriz[2][2]

        # PRINTS : 

print('=-' * 15)
for c in range(3):
    print(f'[ {matriz[c][0]} ] [ {matriz[c][1]} ] [ {matriz[c][2]} ]')

print('=-' * 15)
print(f'A soma de todos os valores pares é igual a {somapar}')
print(f'A soma dos valores da terceira coluna é igual a {soma}')
print(f'O maior valor da segunda linha é {maior}')
