"""
Draw a square spirall
"""

import turtle

T = turtle.Pen()
T.speed(100)
T.color("lightblue")

for x in range(1000):
    T.circle(x)
    T.left(90) 