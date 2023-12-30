from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


my_label = Label(text="Timer", font=(FONT_NAME,30,'bold'))
my_label.pack()
my_label.config(bg=YELLOW,fg=GREEN)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
my_tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=my_tomato_img)
canvas.create_text(103,132,text="00:00", fill="white", font=(FONT_NAME, 13,"bold"))
canvas.pack()

start_button = Button(text="Start")
start_button.pack()

reset_button = Button(text="Reset")
reset_button.pack()



window.mainloop()