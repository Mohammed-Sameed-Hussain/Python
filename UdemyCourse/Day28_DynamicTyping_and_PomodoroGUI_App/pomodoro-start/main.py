from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
def timer_initiate(*reset):
    if len(reset) == 0 :
        count_down(1800)
    else:
        count_down(0)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if 0<=seconds<10 :
        seconds = "0"+str(seconds)
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

my_label = Label(text="Timer", font=(FONT_NAME, 30, 'bold'))
my_label.config(bg=YELLOW, fg=GREEN)
my_label.grid(column=2, row=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
my_tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=my_tomato_img)
timer_text = canvas.create_text(103, 132, text="00:00", fill="white", font=(FONT_NAME, 13, "bold"))
canvas.grid(column=2, row=2)

start_button = Button(text="Start", command=timer_initiate)
start_button.grid(column=1, row=3)

reset_button = Button(text="Reset", command=time_reset)
reset_button.grid(column=3, row=3)

check_marks = Label(text='✔', fg=GREEN, bg=YELLOW)
check_marks.grid(column=2, row=3)

window.mainloop()
