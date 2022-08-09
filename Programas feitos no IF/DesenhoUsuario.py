import turtle
from time import sleep

t = turtle.Turtle() 

while True:
    print('[1] Esqerda\n[2] Frente\n[3] Direita\n[4] Trás')
    print('(Digite qualquer outro valor para sair)')

    lado = int(input('Qual lado deseja ir?'))

    if lado == 1:
        t.left(90)
        t.forward(50)
    elif lado == 2:
        t.forward(50)
    elif lado == 3:
        t.right(90)
        t.forward(50)
    elif lado == 4:
        t.forward(-50)
    else:
        break