import tkinter

window = tkinter.Tk()

window.title("My First GUI Program")
window.minsize(width=1500, height=600)  # in pixels

# Label
my_label = tkinter.Label(text="I am a label", font=("Times New Roman", 24, 'bold'))
my_label.pack()


def button_clicked():
    # print("I got clicked")
    my_label.config(text=Input.get())

my_label["text"] = "altered text"
my_label.config(text="second altered text")

button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()


# Entry
Input = tkinter.Entry(width=30)

Input.pack()





















window.mainloop()

