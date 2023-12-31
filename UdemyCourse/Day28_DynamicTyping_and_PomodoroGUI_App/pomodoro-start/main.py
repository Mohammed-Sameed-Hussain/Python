from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1 / 6
SHORT_BREAK_MIN = 1 / 6
LONG_BREAK_MIN = 1 / 6
REPS = 0
timer = None


# mark = ""

# ---------------------------- TIMER RESET ------------------------------- #
def timer_reset():
    global timer
    global REPS
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    my_label.config(text="TIMER")
    check_marks.config(text="")
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def timer_initiate():
    global REPS
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 2 == 0 and REPS < 7:
        print("in work statement")
        my_label.config(fg=GREEN, text="WORK")
        count_down(work_sec)
        REPS = REPS + 1
    elif REPS == 7:
        my_label.config(fg=RED, text="LONG BREAK")
        count_down(long_break_sec)
        REPS = 0
        return
    else:
        print("in short break statemnt")
        my_label.config(fg=PINK, text="SHORT BREAK")
        count_down(short_break_sec)
        REPS = REPS + 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global timer
    minutes = math.floor(count / 60)
    seconds = count % 60
    if 0 <= seconds < 10:
        seconds = "0" + str(seconds)
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    elif REPS == 7:
        mark = ""
        for _ in range(math.floor((REPS + 1) / 2)):
            mark = mark + "✔"
        check_marks.config(text=mark)
        timer_initiate()
        return
    elif count == 0:
        # timer_initiate()
        mark = ""
        for _ in range(math.floor((REPS + 1) / 2)):
            mark = mark + "✔"
        check_marks.config(text=mark)
        timer_initiate()


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

reset_button = Button(text="Reset", command=timer_reset)
reset_button.grid(column=3, row=3)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=2, row=3)

window.mainloop()
