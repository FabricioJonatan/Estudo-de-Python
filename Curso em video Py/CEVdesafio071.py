print('==' * 20)
print('       BANCO DO FODA DO FABRICIO!')
print('==' * 20, '\n')

saque = int(input('Qual valor deseja sacar? R$ '))
n50 = n20 = n10 = n1 = 0

            # SEPARAÇÃO DAS CEDAS
while True:
    if saque - 50 < 0:
        break
    
    saque -= 50
    n50 += 1

while True:
    if saque - 20 < 0:
        break

    saque -= 20
    n20 += 1

while True:
    if saque - 10 < 0:
        break

    saque -= 10
    n10 += 1

while True:
    if saque - 1 < 0:
        break

    saque -= 1
    n1 += 1
    
if n50 != 0:
    print(f'Total de cédulas de R$ 50.00 : {n50}')
if n20 != 0:
    print(f'Total de cédulas de R$ 20.00 : {n20}')
if n10 != 0:
    print(f'Total de cédulas de R$ 10.00 : {n10}')
if n1 != 0:
    print(f'Total de cédulas de R$ 1.00 : {n1}')
print('==' * 20, '\n')
print('Obrigado e volte sempre ao BANCO FODA! Bom dia!')