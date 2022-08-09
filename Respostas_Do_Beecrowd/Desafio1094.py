cont = int(input())
coe = 0
sap = 0
rat = 0

        #   Quantidade e tipos de cobaias
for c in range(1, cont + 1):
    quant, cobaia = input().split()
    cobaia = cobaia.lower()
    quant = int(quant)

    if cobaia == 'c':
        coe += quant
    elif cobaia == 'r':
        rat += quant
    else:
        sap += quant

        #    Porcentagem do tipo de Cobaias
total = rat + sap + coe
ratp = (rat / total) * 100
sapp = (sap / total) * 100
coep = (coe / total) * 100
    
print('Total: {} cobaias'.format(total))
print('Total de coelhos: {}'.format(coe))
print('Total de ratos: {}'.format(rat))
print('Total de sapos: {}'.format(sap))
print('Percentual de coelhos: {:.2f} %'.format(coep))
print('Percentual de ratos: {:.2f} %'.format(ratp))
print('Percentual de sapos: {:.2f} %'.format(sapp))