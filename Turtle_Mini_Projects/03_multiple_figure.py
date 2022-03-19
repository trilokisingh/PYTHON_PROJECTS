import random
from turtle import Turtle, Screen
from random import Random


tommy = Turtle()
ext = Screen()
tommy.pensize(5)
#*****************************************************************************************************
# tommy.pencolor("red")
#
# for _ in range(0, 4):
#     tommy.forward(100)
#     tommy.left(90)
#
# tommy.pencolor("black")
# tommy.forward(100)
# for _ in range(0, 5):
#
#     tommy.left(72)
#     tommy.forward(100)
#***********************************************************************************************************/
tommy.speed("slow")

def dra_fig(num_side):

    tommy.color(random.choice(color))
    angle = 360 / num_side
    for _ in range(num_side):

        tommy.forward(50)
        tommy.left(angle)


color = ["red", "green", "black", "pink","yellow"]


for num_side in range(3, 10):

    dra_fig(num_side)


ext.exitonclick()