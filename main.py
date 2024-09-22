from turtle import *

v = 100 #швидкість черепашки

t = Turtle()
t.color('blue')
t.width(5)
t.shape('circle')
t.pendown()
t.speed(v)

def draw(x, y):
   t.goto(x, y)

def move(x, y):
   t.penup()
   t.goto(x, y)
   t.pendown()

def setRed():
   t.color('red')

def setGreen():
   t.color('green')

def setBlue():
   t.color('blue')

def startFill():
   t.begin_fill()

def endFill():
   t.end_fill()

t.ondrag(draw)

scr = t.getscreen()
scr.onscreenclick(move)
scr.onkey(setRed,'r')
scr.onkey(setGreen,'g')
scr.onkey(setBlue,'b')
scr.onkey(startFill,'f')
scr.onkey(endFill,'e')

scr.listen()