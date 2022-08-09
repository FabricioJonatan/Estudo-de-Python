lista = []

while True:
    valor = int(input('Digite um valor pra adicionar a lista : '))
    lista.append(valor)

    while True:
        resposta = input('Você deseja continuar? [S/N] ').strip().lower()

        if resposta in 'ns':
            break
        else:
            print('Resposta inválida! Digite novamente!!')
    if resposta == 'n':
        break

print('=-=' * 20)
print(f'Você digitou {len(lista)} numeros e eles foram adicionados a lista!')
print(f'A lista ordenada de forma decrescente fica assim : {sorted(lista, reverse = True)}!')

if 5 in lista:
    print('O valor "5" se encontra na lista!')
else:
    print('O valor "5" não foi encontrado na lista!')