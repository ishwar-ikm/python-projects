import json
import tkinter
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Function is to generate passwords completely random
def generate_password():
    # List to store all alphabets
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    # List to store numbers
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # List to store symbols
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Randomly choosing number of letters, symbols and numbers
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    # Randomly choosing letters, symbols and numbers from their respective list
    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    # Shuffling the password list to randomise the position of letters, symbols and numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)  # This line will automatically copy the generated password to your clipboard

    return password


# Function called by the generate password button
def display_password():
    pEntry.delete(0, tkinter.END)
    pEntry.insert(0, generate_password())


# ---------------------------- SAVE PASSWORD ------------------------------- #
# Function to add data into the json file format called Password.json
def add_data():
    # Get all the entries and save it inside their respective variables
    website = webEntry.get().title()
    email = mailEntry.get()
    password = pEntry.get()

    # create a dictionary to save the data in json file
    user_data = {
        website: {
            "Email": email,
            "Password": password,
        }
    }

    # Error box to raise error window if the user forgot to enter any one of the entries
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Do not leave any field empty")

    else:
        # Getting user confirmation before entering the data in json file
        is_ok = messagebox.askyesno(title=website, message=f"The fields entered are\nEmail: {email}\nPassword: {password}\nDo you want to save these details?\n")

        if is_ok:
            # Data is added into the json file
            try:
                with open("Password.json", "r") as file:
                    data = json.load(file)
                    
            # If the program is run for the first time and there is no Password.json then this except block will create that file and add the data
            except:  
                with open("Password.json", "w") as file:
                    json.dump(user_data, file, indent=4)

            # If the file exists we want to update the file with the new data
            else: 
                data.update(user_data)
                with open("Password.json", "w") as file:
                    json.dump(data, file, indent=4)  # Add the data into the json file

            # Delete all entries to get ready to take new entries
            finally:
                mailEntry.delete(0, tkinter.END)
                webEntry.delete(0, tkinter.END)
                pEntry.delete(0, tkinter.END)
                webEntry.focus()


# ---------------------------- Search Password ------------------------------- #
# Function to search password in the saved file
def search_password():
    # Read the website entry
    website = webEntry.get().title()

    try:
        with open("Password.json", "r") as file:
            data = json.load(file)
            messagebox.showinfo(title="Your Password", message=f"Detail for {website}: \nEmail: {data[website]['Email']} \nPassword: {data[website]['Password']} \nYour Password is copied to your clipboard")
            pyperclip.copy(data[website]['Password'])  # This line will automatically copy the generated password to your clipboard

    # Will catch the error if there is no data or there is no file created
    except:
        messagebox.showerror(title="Website Not Found", message="The website data you are looking for is not currently available.")

    finally:
        mailEntry.delete(0, tkinter.END)
        webEntry.delete(0, tkinter.END)
        pEntry.delete(0, tkinter.END)
        webEntry.focus()


# ---------------------------- UI SETUP ------------------------------- #

# Window
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
webEntry = tkinter.Entry(width=34)
webEntry.focus()
webEntry.grid(row=2, column=2)

mailEntry = tkinter.Entry(width=52)
mailEntry.grid(row=3, column=2, columnspan=2)

pEntry = tkinter.Entry(width=34)
pEntry.grid(row=4, column=2)


# Buttons
add = tkinter.Button(text="Add", width=44, command=add_data)
add.grid(row=5, column=2, columnspan=2)

gen = tkinter.Button(text="Generate Password", command=display_password)
gen.grid(row=4, column=3)

search = tkinter.Button(text="Search", width=14, command=search_password)
search.grid(row=2, column=3)


window.mainloop()
