from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for i in range(randint(8, 10))]
    password_list += [choice(symbols) for i in range(randint(2, 4))]
    password_list += [choice(numbers) for i in range(randint(2, 4))]

    # from random module
    shuffle(password_list) 

    password = "".join(password_list)
   
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    
    pyperclip.copy(password)
    


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    web = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    if len(web) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title=None, message="One or more field is empty")
    else:
        check2 = messagebox.askokcancel(title=web, message=f"You entered\nEmail: {email}\nPassword: {password}\nWebsite: {web}\nDo you wish to save")
        if check2 == True:
            with open("data.txt", "a") as data:
                data.write(f"{web} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
    
    website_entry.focus()
        


# ---------------------------- UI SETUP ------------------------------- #




window = Tk()
window.title("PASSWORD MANAGER")
window.minsize(width=500, height=400)
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)


website = Label(text="Website:")
website.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()



email = Label(text="Email/Username:")
email.grid(column=0, row=2)

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(END, string="imkp004@gmail.com")


password = Label(text="Password:")
password.grid(column=0, row=3)

password_entry = Entry(width=20)
password_entry.grid(column=1, row=3)


Generate = Button(text="Generate Password", width=11, command=generate_password)
Generate.grid(column=2, row=3)
Generate.config(padx=0)

add = Button(text="Add", width=33, command=save_data)
add.grid(column=1, row=4, columnspan=2)


window.mainloop()


