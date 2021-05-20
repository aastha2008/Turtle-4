'''
04/01/2021

Python Function
-Bundle a set of code that you want to use repeatedly 

Define a Function

1)
def FUNCTIONNAME():
  BODY

2)
def FUNCTIONNAME(PARAMETER):
  BODY w/ PARAMETER


import turtle

#setup a turtle or a pen 
pen=turtle.Turtle()

def drawSquare():
  pen.fd(100)
  pen.left(90)
  pen.fd(100)
  pen.left(90)
  pen.fd(100)
  pen.left(90)
  pen.fd(100)
  pen.left(90)

def drawSquare2(l):
  pen.fd(l)
  pen.left(90)
  pen.fd(l)
  pen.left(90)
  pen.fd(l)
  pen.left(90)
  pen.fd(l)
  pen.left(90)

drawSquare()
drawSquare2(50)

circle(radius,angle,sides)


import turtle
import random

#setup a turtle or a pen
pen=turtle.Turtle()

def drawShapes(radius, side):
  pen.circle(radius, 360, side)

drawShapes(100, 3)
drawShapes(90, 6)



for i in range(10):
  pen.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
  drawShapes(100, 3+i)
  '''

import turtle
import random

#Start out with showing the game
#Setup turtle to draw

t1 = turtle.Turtle()
t1.color("red")
t1.speed(100)

x=-140
y=140

t1.penup()
t1.goto(x,y)


for i in range(16):
  t1.pendown()
  t1.write(i)

  t1.penup()
  t1.right(90)
  t1.fd(10)

  t1.pendown()
  t1.fd(150)

  t1.penup()
  t1.goto(x + (20 * (i+1)), 140)
  t1.left(90)

# turtle1
t1.color(random.randint(0,255),random.randint(0,255), random.randint(0,255))
t1.shape("turtle")
t1.penup()
t1.goto(-155,100)
t1.pendown()

#turtle2 (-155,70)
t2=turtle.Turtle()
t2.color(random.randint(0,255),random.randint(0,255), random.randint(0,255))
t2.shape("turtle")
t2.penup()
t2.goto(-155,70)
t2.pendown()

#turtle3 (-155,40)
t3=turtle.Turtle()
t3.color(random.randint(0,255),random.randint(0,255), random.randint(0,255))
t3.shape("turtle")
t3.penup()
t3.goto(-155,40)
t3.pendown()

#turtle4 (-155,10)
t4=turtle.Turtle()
t4.color(random.randint(0,255),random.randint(0,255), random.randint(0,255))
t4.shape("turtle")
t4.penup()
t4.goto(-155,10)
t4.pendown()

for t in range(105):
  t1.fd(random.randint(1,5))
  t2.fd(random.randint(1,5))
  t3.fd(random.randint(1,5))
  t4.fd(random.randint(1,5))


