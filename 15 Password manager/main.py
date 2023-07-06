import tkinter
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)

    return password


def display_password():
    pEntry.delete(0, tkinter.END)
    pEntry.insert(0, generate_password())


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
    website = webEntry.get()
    email = mailEntry.get()
    password = pEntry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Do not leave any field empty")

    else:
        is_ok = messagebox.askyesno(title=website, message=f"The fields entered are\nEmail: {email}\nPassword: {password}\nDo you want to save these details?\n")

        if is_ok:
            with open("Password.txt", mode="a") as file:
                file.write(f"{website} | {email} | {password}\n")
            mailEntry.delete(0, tkinter.END)
            webEntry.delete(0, tkinter.END)
            pEntry.delete(0, tkinter.END)
            webEntry.focus()


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200)
img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=1, column=2)

# Labels
web = tkinter.Label(text="Website: ", font=("Arial", 13, "normal"))
web.grid(row=2, column=1)

mail = tkinter.Label(text="Email/Username: ", font=("Arial", 13, "normal"))
mail.grid(row=3, column=1)

pw = tkinter.Label(text="Password: ", font=("Arial", 13, "normal"))
pw.grid(row=4, column=1)

# Entries
webEntry = tkinter.Entry(width=52)
webEntry.focus()
webEntry.grid(row=2, column=2, columnspan=2)

mailEntry = tkinter.Entry(width=52)
mailEntry.grid(row=3, column=2, columnspan=2)

pEntry = tkinter.Entry(width=34)
pEntry.grid(row=4, column=2)

add = tkinter.Button(text="Add", width=44, command=add_data)
add.grid(row=5, column=2, columnspan=2)

gen = tkinter.Button(text="Generate Password", command=display_password)
gen.grid(row=4, column=3)


window.mainloop()