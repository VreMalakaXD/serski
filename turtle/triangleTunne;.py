from turtle import Turtle
import random as r
import math
t = Turtle()
t.speed(100)
xSize = 300
ySize = 300
resolution = 5
t.screen.screensize(ySize*2,xSize*2)

def Triangle(Size):
    if Size < resolution:
        pass
    else:
        t.penup()
        t.goto(0,0)
        side = (2/3) * (3 ** (3/4)) * math.sqrt(Size)
        t.seth(90)
        t.back(((math.sqrt(3)/2) * side)/2)
        t.seth(0)
        t.forward(side/2)
        t.seth(180)
        t.pendown()
        t.forward(side)
        t.right(120)
        t.forward(side)
        t.right(120)
        t.forward(side)
        t.penup()
        t.goto(0,0)
        Triangle(Size/1.2)
Triangle(50000000)
t.screen.mainloop()
