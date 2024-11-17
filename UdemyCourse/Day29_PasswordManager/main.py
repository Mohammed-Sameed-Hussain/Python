from random import shuffle
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
from matplotlib.pyplot import title


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]


    password_list = password_letters+password_symbols+password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)

# print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) ==0 or  len(password) ==0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"These are the details entered: \nEmail:{email} \n Password: {password}\n Is it ok to save?")


        if is_ok:
            with open("data.txt","a") as f:
                f.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.title("Password Manager")
window.config(padx=50,pady=20)

canvas = Canvas(height=200, width=200)
logo_imp = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_imp)
canvas.grid(row=0,column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1,column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2,column=0)

password_label = Label(text="Password:")
password_label.grid(row=3,column=0)

# Entries

website_entry = Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)

email_entry = Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"sameedhussain202@gmail.com")

password_entry = Entry(width=16)
password_entry.grid(row=3,column=1,columnspan=1)


# Button
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3,column=2)

add_button = Button(text="Add",width=32, command=save)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()