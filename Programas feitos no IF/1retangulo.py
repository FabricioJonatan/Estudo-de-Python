import turtle
from time import sleep

base = int(input('escolha o tamanho da base : '))
altura = int(input('escolha o tamanho da altura : '))
t = turtle.Turtle()

t.forward(base)
t.left(90)
t.forward(altura)
t.left(90)
t.forward(base)
t.left(90)
t.forward(altura)

sleep(2.0)