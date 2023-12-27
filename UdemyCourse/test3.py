import time
from turtle import Turtle, Screen

screen = Screen()

my_turtle = Turtle()
my_turtle.penup()
my_turtle.speed(0)
my_turtle.hideturtle()
my_turtle.goto(0, 320)
my_turtle.write("My Score:", False, "center", ('Arial', 12, 'bold'))

screen.exitonclick()
