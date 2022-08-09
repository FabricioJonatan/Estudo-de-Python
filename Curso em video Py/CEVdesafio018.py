import math

angulo = float(input('Digite o âgulo que deseja :'))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangene = math.tan(math.radians(angulo))

print('O Seno deste ângulo é : {:.2f} \nO Cosseno deste ângulo é : {:.2f}'.format(seno, cosseno))
print('A tangente deste ângulo é : {:.2f}'.format(tangene))