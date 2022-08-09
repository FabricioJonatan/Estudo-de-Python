matriz = []

for linha in range(3):
    valor1 = int(input(f'Digite o valor para [{linha}, 0] : '))
    valor2 = int(input(f'Digite o valor para [{linha}, 1] : '))
    valor3 = int(input(f'Digite o valor para [{linha}, 2] : '))
    line = [valor1, valor2, valor3]
    matriz.append(line)

print('=-' * 15)

for c in range(3):
    print(f'[ {matriz[c][0]} ] [ {matriz[c][1]} ] [ {matriz[c][2]} ]')