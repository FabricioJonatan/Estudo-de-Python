media, quant, maior, resposta = 0, 0, 0, 's'

while resposta != 'n':
    numero = int(input('Digite um numero : '))
    resposta = input('Deseja continuar? [digite "n" para encerrar] '.strip().lower())
    print('=-' * 30)

    if numero > maior:
        maior = numero
    if quant == 0:
        menor = numero
    else:
        if numero < menor:
            menor = numero
    
    quant += 1
    media += numero / 2

print('Você digitou {} valores e a MEDIA destes valores é {}'.format(quant, media))
print('O maior valor digitado é {} e o menor é {}'.format(maior, menor))