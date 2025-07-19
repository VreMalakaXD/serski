from turtle import Turtle
import random as r
import math
t = Turtle()
t.speed(10)
t.screen.title("Turtle testing")
xSize = 300
ySize = 300
resolution = 5
t.screen.screensize(ySize*2,xSize*2)
t.screen.colormode(255)

def genRandomColor():
    red = r.randint(0,255)
    g = r.randint(0,255)
    b = r.randint(0,255)
    return (red,g,b)

def square (centerX,centerY ,size,lineColor,fillColor,lineWidth):
    t.penup()
    t.setpos(centerX,centerY)
    t.pendown()
    t.color(lineColor,fillColor)
    t.width(lineWidth)
    t.penup()
    t.forward(size/2)
    t.left(90)
    t.forward(size/2)
    t.left(90)
    t.pendown()
    t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()
t.penup()
t.pendown()
'''
square(0,0,500,genRandomColor(),genRandomColor(),r.randint(1,10))
square(-50,-150,100,genRandomColor(),genRandomColor(),r.randint(1,10))
square(150,150,50,genRandomColor(),genRandomColor(),r.randint(1,10))
'''
Cols = 10
rows = 10

t.color(0,0,0)
for i in range(0,Cols+1):
    SideInc = (t.screen.window_width()) / Cols
    t.penup()
    t.setpos((-t.screen.window_width()/2)+(i*SideInc),(t.screen.window_height()/2))
    t.pendown()
    t.setpos((-t.screen.window_width()/2)+(i*SideInc),(-t.screen.window_height()/2))
for i in range(0,rows+1):
    SideInc = (t.screen.window_width()) / rows
    t.penup()
    t.setpos((t.screen.window_width() / 2)- (i*SideInc), (t.screen.window_height() / 2)- (i*SideInc))
    t.pendown()
    t.setpos((-t.screen.window_width() / 2), (t.screen.window_height() / 2)- (i*SideInc))
t.screen.mainloop()