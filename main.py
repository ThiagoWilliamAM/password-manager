import pyperclip
import tkinter as tkr
from tkinter import *
from tkinter import messagebox
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', "@"]

    # nr_letters = random.randint(8, 10)
    # nr_symbols = random.randint(2, 4)
    # nr_numbers = random.randint(2, 4)

    # password_list = []

    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))

    password_list.extend(random.choice(symbols) for _ in range(random.randint(2, 4)))
    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)

    password_list.extend(random.choice(numbers) for _ in range(random.randint(2, 4)))
    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)

    random.shuffle(password_list)

    password_random = "".join(password_list)
    # for char in password_list:
    #     password_random += char

    if len(password_input.get()) < 0:
        password_input.insert(END, f"{password_random}")
    else:
        password_input.delete(0, "end")
        password_input.insert(END, f"{password_random}")

    pyperclip.copy(password_random)
    # print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_state():

    website_line = web_input.get()
    username_line = user_input.get()
    password_line = password_input.get()

    if len(website_line) < 1 or len(username_line) < 1 or len(password_line) < 1:
        messagebox.showerror(title="ERROR", message="type all info!")
    else:
        is_ok = messagebox.askokcancel(title=website_line, message=f"Username: {username_line}\n"
                                                                   f"Password: {password_line}\n"
                                                                   f"OK to confirm, Cancel to return")
        if is_ok:
            file = open("data.txt", "a")
            file.write(f"{website_line}  |  {username_line}  |  {password_line} \n")
            web_input.delete(0, "end")
            user_input.delete(0, "end")
            password_input.delete(0, "end")
            file.close()


# ---------------------------- UI SETUP ------------------------------- #


# WINDOW
window = tkr.Tk()
window.title("Password Storage")
window.config(pady=40, padx=50)

# LOCK CANVAS

canvas = tkr.Canvas(width=200, height=200)
lock_img = tkr.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# WEBSITE INPUT AND LABEL

website = tkr.Label(text="Website")
website.grid(row=1, column=0)
web_input = tkr.Entry(width=35, border=3)
web_input.grid(row=1, column=1, columnspan=2, sticky="ew", pady=5)

# EMAIL/USER NAME INPUT AND LABEL

username = tkr.Label(text="Username/E-mail  ")
username.grid(row=2, column=0)
user_input = tkr.Entry(width=35, border=3)
user_input.insert(END, "username@server.com")
user_input.grid(row=2, column=1, columnspan=2, sticky="ew", pady=5)

# PASSWORD INPUT AND LABEL

password = tkr.Label(text="Password")
password.grid(row=3, column=0, pady=10)
password_input = tkr.Entry(width=21, border=3)
password_input.grid(row=3, column=1, pady=2, sticky="ew")

# GENERATE PASSWORD BUTTON

gen_password = tkr.Button(text="Generate Password", border=3, relief="raised", command=password_gen)
gen_password.grid(row=3, column=2, pady=2)

# GENERATE ADD BUTTON

add = tkr.Button(text="Add", width=44, command=save_state, borderwidth=3, relief="raised")
add.grid(row=4, column=1, columnspan=2, pady=2)


window.mainloop()
