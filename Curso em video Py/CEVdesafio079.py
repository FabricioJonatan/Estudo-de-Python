valores = []

while True:
    valor = int(input('Digite um valor : '))

    if valor in valores:
        print('Valor duplicado, não adicionarei a lista!')
    else:
        print('Valor adicionado com sucesso a lista!!')
        valores.append(valor)
    
    while True:
        resposta = input('Deseja continuar? [S/N] : ').strip().lower()

        if resposta in 'sn': break
        else : print('Resposta inválida, digite novamente.')
    
    if resposta == 'n' : break

valores.sort()
print('=-' * 20)
print(f'Você digitou os valores {valores}')
