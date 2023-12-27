from turtle import Screen
import turtle
import pandas

screen = Screen()
screen.title("US States Game")

img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

states_data = pandas.read_csv("50_states.csv")
US_states = states_data["state"].to_list()
# x_co_ordinates = states_data["x"]
# y_co_ordinates = states_data["y"]

no_of_correct_states = 0

my_turtle = turtle.Turtle()
my_turtle.penup()
my_turtle.hideturtle()
guessed_states = []

while no_of_correct_states != 50:
    user_answer_input = screen.textinput(title=f"{no_of_correct_states}/50 States Correct",
                                         prompt="What's the next " "state?")
    if user_answer_input == 'exit' or "Exit":
        missing_states = [state for state in US_states if state not in guessed_states]
        break
    for answer_state in US_states:
        if user_answer_input.lower() == answer_state.lower():
            no_of_correct_states = no_of_correct_states + 1
            guessed_states.append(answer_state)
            data = states_data[states_data.state == answer_state]
            my_turtle.goto(int(data.x), int(data.y))
            my_turtle.write(f"{user_answer_input}")

screen.exitonclick()
