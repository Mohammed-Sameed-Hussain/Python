from turtle import Turtle,Screen
import turtle
import random


is_race_on = False

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput("Make your bet","Which turtle will win the race? Enter a color:")


colors = ['red','orange','yellow','green','blue','purple']

all_turtles = []
i=0
for colours in colors:
    all_turtles.append(Turtle("turtle"))
    all_turtles[i].color(colours)
    all_turtles[i].penup()
    all_turtles[i].goto(-230,-150+50*i)
    i=i+1


if user_bet:
    is_race_on = True



while is_race_on:
    for i in range(0,6):
        all_turtles[i].forward(random.randint(0,10))

    for i in range(0,6):
        if all_turtles[i].pos()[0] >= 230 :
            is_race_on = False
            print(f"{colors[i]} turtle won")
            if user_bet==colors[i]:
                print("You won the bet! :)")
            else:
                print("You lost the bet! :(")
            break








screen.exitonclick()