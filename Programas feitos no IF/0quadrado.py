import turtle
from time import sleep

base = int(input('escolha o tamanho do lado : '))
t = turtle.Turtle()

t.forward(base)
t.left(90)
t.forward(base)
t.left(90)
t.forward(base)
t.left(90)
t.forward(base)

sleep(2.0)