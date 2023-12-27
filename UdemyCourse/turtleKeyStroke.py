from turtle import Turtle, Screen

my_turtle = Turtle()
screen = Screen()

screen.listen()
def move_forward():
    my_turtle.forward(10)

def move_bakcward():
    my_turtle.back(10)


def counter_clockwise():
    my_turtle.left(15)

def clock_wise():
    my_turtle.right(15)

def clear_drawing():
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()



screen.onkey(move_forward, "w")
screen.onkey(move_bakcward, "s")
screen.onkey(counter_clockwise, "a")
screen.onkey(clock_wise, "d")
screen.onkey(clear_drawing, "c")

screen.exitonclick()
