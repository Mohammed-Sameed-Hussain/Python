import tkinter

window = tkinter.Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=300)  # in pixels

# Label
my_label = tkinter.Label(text="I am a label", font=("Times New Roman", 24, 'bold'))
my_label.pack()

window.mainloop()
