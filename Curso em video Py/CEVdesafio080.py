valores = []

for cont in range(5):
    valor = int(input('Digite um valor : '))

    if cont == 0 or valor > valores[-1]:
        valores.append(valor)
        print('Adicionado ao final da lista. . .')
    else:
        posição = 0

        while posição < len(valores):
            if valor < valores[posição]:
                valores.insert(posição, valor)
                print(f'Adicionado na {posição}° posição da lista. . .')
                break

            posição += 1

print('=-' * 20)
print(f'Os valores organizados em ordem são {valores}')