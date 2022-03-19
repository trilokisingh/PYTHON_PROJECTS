import turtle
import random


def crl_clr():   # for pickup the random color
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    col = (r, g, b)
    return col


crl = turtle.Turtle()
turtle.colormode(255) # this is important for pickuping the random color rangr 255
time = turtle.Screen()
crl.speed("fastest")
crl.pensize(2)

def spirolograf(size):
    for _ in range(int(360/size)):
        crl.color(crl_clr())  # this is the call of function
        crl.circle(100)
        crl.setheading(crl.heading()+size)   # set the new position of circle


spirolograf(5)
time.exitonclick()
