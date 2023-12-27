from turtle import Turtle, Screen
import turtle
import random


my_turtle = Turtle()

my_turtle.speed("fastest")

turtle.colormode(255)


color_list = [(139, 81, 60), (24, 31, 54), (47, 89, 148), (47, 29, 36), (29, 56, 116), (191, 140, 103), (65, 34, 29), (98, 48, 40), (111, 79, 87), (119, 150, 191), (170, 112, 93), (93, 122, 175), (86, 50, 55), (171, 142, 153), (232, 210, 187), (176, 123, 73), (206, 216, 241), (153, 112, 122), (228, 210, 224), (228, 196, 137), (172, 179, 229), (215, 182, 173), (237, 248, 244), (211, 178, 199), (20, 26, 22), (86, 64, 35), (65, 142, 186), (158, 170, 164), (94, 102, 100), (168, 200, 211), (176, 200, 192), (54, 48, 208), (35, 70, 90)]
my_turtle.hideturtle()

for i in range(1,101):
    my_turtle.color(random.choice(color_list))
    my_turtle.dot(15)
    my_turtle.penup()
    my_turtle.forward(30)
    my_turtle.pendown()
    if i%10 ==0:
        my_turtle.penup()
        my_turtle.setx(0)
        my_turtle.sety(30*(i/10))
        my_turtle.pendown()


screen = Screen()

screen.exitonclick()