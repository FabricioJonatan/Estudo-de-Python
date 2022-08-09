import turtle
from time import sleep

degrau = int(input('escolha o tamanho da escada : '))
base = degrau*3
t = turtle.Turtle()

t.forward(base)
t.left(90)
t.forward(base)
t.left(90)
t.forward(degrau)
t.left(90)
t.forward(degrau)
t.left(-90)
t.forward(degrau)
t.left(90)
t.forward(degrau)
t.left(-90)
t.forward(degrau)
t.left(90)
t.forward(degrau)

sleep(2.0)