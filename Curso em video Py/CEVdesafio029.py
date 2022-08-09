velocidade = float(input('Qual a velocidade atual do carro? '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('\033[4;31mMULTADO!\033[0;31m Você excedeu o limite permitido que é 80 km/h\nVocê deverá pagar uma multa de {:.2f} R$\033[m'.format(multa))
else:
    print('\033[4;32mMuito bem!\033[0;32m Você esta dentro dos limites permitidos!')
print('\033[33mTenha um bom dia! Dirija com cuidado!\033[m')