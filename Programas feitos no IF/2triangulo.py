import turtle
from time import sleep

lado = int(input('escolha o tamanho do lado : '))
t = turtle.Turtle()

t.forward(lado)
t.left(120)
t.forward(lado)
t.left(120)
t.forward(lado)

sleep(2.0)