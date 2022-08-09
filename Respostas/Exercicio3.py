#   Crie um programa onde o usuário possa digitar vários
# valores numéricos e coloque-os em uma lista. Caso o
# número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados.
















numeros = []

while True:
    numero = int(input('Digite algum numero [digite 999 pra parar]: '))

    if numero in numeros:
        print('Este numero já está na lista, não irei adicionar.')
    elif numero == 999:
        break
    else:
        print('Numero adicionado com sucesso!')
        numeros.append(numero)
    
print(f'Os valores adicionados a lista foram {numeros}')