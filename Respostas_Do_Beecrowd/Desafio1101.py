maior = 0
menor = 0

while True:
    valor1, valor2 = map(int, input().split())
   
    if valor1 <= 0 or valor2 <= 0:
        break
    if valor1 > valor2:
        maior = valor1
        menor = valor2
    else:
        maior = valor2
        menor = valor1
               
    soma = 0
       
    while menor <= maior :
         print(menor, end=' ')
         soma += menor
         menor += 1
    print("Sum={}".format(soma))