"""
Draw a octagon spirall
"""
colors = ["red","darkred","lightgreen","blue","darkblue","lightblue","green","yellow","purple"]
import turtle
from time import sleep

T = turtle.Pen()
turtle.bgcolor('black')
T.speed(100)
T.width(10)


for x in range(300):
    T.pencolor(colors[x%9])
    T.forward(x)
    T.left(45)

sleep(20)