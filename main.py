import tkinter
import random
from tkinter import messagebox
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def randompass():
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
    passin.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def savepassword():
    dictionary = {}
    dictionary[webin.get()] = {'email': emailin.get(), 'password': passin.get()}
    try:
        with open("passwords.json", mode='r') as file:
            data = json.load(file)
            data.update(dictionary)
    except:
        with open("passwords.json", mode='w') as file:
            json.dump(dictionary, file, indent=4)
    else:
        with open("passwords.json", mode='w') as file:
            json.dump(data, file, indent=4)

    webin.delete(0, len(webin.get()))
    passin.delete(0, len(passin.get()))

def searchaccount():
    try:
        with open("passwords.json", mode='r') as file:
            data = json.load(file)
            emailin.insert(0,data[webin.get()]['email'])
            passin.insert(0, data[webin.get()]['password'])
    except:
        messagebox.showinfo(title='search result', message='No email found')

def save():
    if len(webin.get()) * len(emailin.get()) * len(passin.get()) == 0:
        messagebox.showinfo(title='oops!', message='Please enter all the details...')
        webin.delete(0, len(webin.get()))
        passin.delete(0, len(passin.get()))
        emailin.delete(0, len(emailin.get()))
    elif messagebox.askokcancel(title='Save the details?',
                                message=f'Website:{webin.get()} \nEmail:{emailin.get()} \nPassword:{passin.get()} \n') == True:
        savepassword()


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title('Password Manager')
window.config(padx=20, pady=50)
window.minsize(width=600, height=450)
window.maxsize(width=600, height=450)

image = tkinter.PhotoImage(file="logo.png")

canvas = tkinter.Canvas(width=200, height=200)
logo = canvas.create_image(100, 100, image=image)

website = tkinter.Label(text="Website :", font=('Arial', 10, 'bold'))
search = tkinter.Button(text='Search', width=15, command=searchaccount)
email = tkinter.Label(text="Email     :", font=('Arial', 10, 'bold'))
password = tkinter.Label(text="Password:", font=('Arial', 10, 'bold'))

webin = tkinter.Entry()
webin.config(width=30)
emailin = tkinter.Entry()
emailin.config(width=50)
passin = tkinter.Entry()
passin.config(width=30)

button = tkinter.Button(text="Generate Password", command=randompass)
add = tkinter.Button(text='Add', width=42, command=save)

add.place(x=175, y=320)
button.place(x=375, y=275)
search.place(x=375, y=215)
webin.place(x=180, y=220, height=20)
emailin.place(x=180, y=250, height=20)
passin.place(x=180, y=280, height=20)
canvas.place(x=180, y=0)
website.place(x=50, y=220)
email.place(x=50, y=250)
password.place(x=50, y=280)

window.mainloop()
