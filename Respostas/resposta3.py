valortotal = 0
pedidos = []

print(f'===== PEDIDO LANCHONETE =====')

print(f'===== Tabela de preços =====')

print('Especificação  Código  Preço')

print('Cachorro quente  100   R$ 1,20')
print('Bauru Simples    101   R$ 1,30')
print('Bauru com Ovo    102   R$ 1,50')
print('Hambúrguer       103   R$ 1,20')
print('Cheeseburguer    104   R$ 1,30')
print('Refrigerante     105   R$ 1,00')
print('=================================')

quantidade1 = int(input('\n   Quantos itens deseja comprar? '))
 
for pedido in range(quantidade1):

    print('Entre com o código do pedido e sua quantidade: ')
    codigo = int(input('Código : '))
    quantidade2 = int(input('Quantidade : '))
    
    if codigo == 100:
        print('Cachorro Quente\n')
        valor = 1.20 * quantidade2
        valortotal += valor
    elif codigo == 101:
        print('Bauru Simples\n')
        valor = 1.30 * quantidade2
        valortotal += valor
    elif codigo == 102:
        print('Bauru com Ovo\n')
        valor = 1.50 * quantidade2
        valortotal += valor
    elif codigo == 103:
        print('Hambúrguer\n')
        valor = 1.20 * quantidade2
        valortotal += valor
    elif codigo == 104:
        print('Cheeseburguer\n')
        valor = 1.30 * quantidade2
        valortotal += valor
    elif codigo == 105:
        print('Refrigerante\n')
        valor = 1.00 * quantidade2
        valortotal += valor

    pedido_todo = [pedido + 1, codigo, quantidade2, valor]
    pedidos.append(pedido_todo)
    print(pedidos)

#PROCESSAMENTO

print(f'======= RESULTADO =======')
print('Pedido  Código  Quantidade  Valor')

#SAÍDA
for pedido in range(len(pedidos)):
    print(f'{pedidos[pedido][0]}         {pedidos[pedido][1]}       {pedidos[pedido][2]}        {pedidos[pedido][3]}')
print('=========================================')
print(f'Total a pagar : R$ {valortotal:.2f}')
print('     {===== FIM DO PROGRAMA =====}     ')