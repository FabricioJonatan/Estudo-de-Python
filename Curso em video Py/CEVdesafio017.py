from math import sqrt

a = float(input('Qual o tamanho do cateto do triangulo :'))
b = float(input('Qual o tamanho do outro cateto do triangulo :'))
c = sqrt(a ** 2 + b ** 2)

print('O tamanho da hipotenusa deste triangulo é de {:.2f}'.format(c))