from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json
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
	website = website_entry.get().upper()
	email = email_entry.get()
	password = password_entry.get()

	new_data = {
		website: {
			"email": email,
			"password": password
		}
	}

	if len(website) == 0 or len(password) == 0:
		messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
	else:
		try:
			with open("data.json", "r") as data_file:
				data = json.load(data_file)
				data.update(new_data)

			with open("data.json", "w") as data_file:
				json.dump(data, data_file, indent=4)

				website_entry.delete(0, END)
				password_entry.delete(0, END)

		except:
			with open("data.json", "w") as data_file:
				json.dump(new_data, data_file, indent=4)

				website_entry.delete(0, END)
				password_entry.delete(0, END)

	website_entry.focus()






def search_website():
	website = website_entry.get().upper()
	web = website_entry.get()
	try:
		with open("data.json", "r") as data_file:
			data = json.load(data_file)

		try:
			messagebox.showinfo(title=website, message=f"You already have this website information saved\nWebsite: {web}\nEmail: {data[website]["email"]}\nPassword: {data[website]["password"]}")
		except KeyError:
			messagebox.showinfo(title=website, message=f"{website} not found")

	except:
		messagebox.showinfo(title=None, message=f"You don't have anything saved")


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

website_entry = Entry(width=20)
website_entry.grid(column=1, row=1)
website_entry.focus()

Search = Button(text="Search", width=10, command=search_website)
Search.grid(column=2, row=1)


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


