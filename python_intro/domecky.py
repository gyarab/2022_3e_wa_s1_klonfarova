from turtle import exitonclick, forward, right, left, shape, goto, pendown, penup
from math import sqrt
from random import randint

shape ('turtle')
penup()
goto(-400,0)
pendown()

def nakresli(a):

    
    left(90)
    forward(a)
    right(90)
    forward(a)
    right(135)
    forward(sqrt(a*a * 2))
    left(135)
    forward(a)
    left(90)
    forward(a)

    left(45)
    forward((a/100)*72)
    left(90)
    forward((a/100)*72)
    left(90)
    forward(sqrt(a*a + a*a))
    
    

    penup()
    forward(randint(10,50))
    pendown()
    

nakresli(randint(50, 180))
nakresli(randint(50, 180))
nakresli(randint(50, 180))
nakresli(randint(50, 180))
nakresli(randint(50, 180))
nakresli(randint(50, 180))
exitonclick()