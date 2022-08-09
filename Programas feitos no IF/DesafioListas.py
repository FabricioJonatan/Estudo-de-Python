print('''
O que você deseja?
[ 1 ] Adicionar uma quantidade especifica de valores na lista
[ 2 ] Adicionar um valor indertemidado de valores na lista
[ 3 ] Fechar o programa
''')

escolha = int(input('Sua escolha : '))
lista = []
listaOrganizada = []
contador = 0
menor = -1

            #  SISTEMA QUE RECEBE OS VALORES E ADICIONA A LISTA
while True:
    if escolha == 1:
        quantidade = int(input('Quantos valores deseja adicionar : '))

        for i in range(quantidade):
            valor = int(input('Digite o {}° valor desejado : '.format(i + 1)))
            lista.append(valor)
        break

    elif escolha == 2:
        print('ATENÇÃO : O programa irá fechar quando você digitar o numero 0')

        while True:
            contador += 1
            valor = int(input('Digite o {}° valor desejado : '.format(contador)))
            lista.append(valor)

            if valor == 0:
                break
        break

    elif escolha == 3:
        print('ENCERRANDO . . .')
        break

    else:
        print('Escolha inválida, por favor, digite novamente!')
        escolha = int(input('Sua escolha : '))

print('Sua lista digitada ficou assim :')
for c in range(len(lista)):
    print('{}  '.format(lista[c]), end = '')

c = 0
lista.sort()

print('\nA lista foi organizada e ficou assim : ')

for c in range(len(lista)):
    print('{} -> '.format(lista[c]), end = '')

print('FIM')


        #     PRIMEIRA TENTATIVA   
#      for c in range(len(lista)):
#          numero = lista[c]
#      
#          if numero == menor:
#              nuemro = lista[c]
#      
#          else:
#              for a in range(len(lista)):
#                  if numero >= lista[a]:
#                      menor = lista[a]
#                  else:
#                      maior = lista[a]
#      
#          if c == len(lista):
#              listaOrganizada.append(maior)
#          
#          listaOrganizada.append(numero)
#          print(menor)


        #      SEGUNDA TENTATIVA
#      for c in range(len(lista)):
#          menor = lista[c]
#      
#          for a in range(c + 1, len(lista)):
#              if menor >= lista[a]:
#                  menor = lista[a]
#              
#          c, menor = menor, c