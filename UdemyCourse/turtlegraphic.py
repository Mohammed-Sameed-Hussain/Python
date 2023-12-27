from turtle import Turtle, Screen
import random
import turtle

turtle.colormode(255)
direction = [0,90,180,270,360]

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    tuple_rgb=(r,g,b)
    return tuple_rgb

my_turtle = Turtle()
my_turtle.pensize(15)
my_turtle.speed(10)
for i in range(0,200):
    my_turtle.color(random_color())
    my_turtle.forward(30)
    my_turtle.right(random.choice(direction))

screen = Screen()
screen.exitonclick()