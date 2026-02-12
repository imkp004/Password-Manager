import streamlit as st
import random
import pyperclip
import os

# ---------------- PASSWORD GENERATOR ---------------- #

def generate_password():
    letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numbers = list("0123456789")
    symbols = list("!#$%&()*+")

    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)
    return "".join(password_list)

# ---------------- SAVE PASSWORD ---------------- #

def save_data(web, email, password):
    with open("data.txt", "a") as file:
        file.write(f"{web} | {email} | {password}\n")

# ---------------- UI ---------------- #

st.title("🔐 Password Manager")

# Input Fields
website = st.text_input("Website")
email = st.text_input("Email / Username", value="imkp004@gmail.com")

# Password field with session storage
if "generated_password" not in st.session_state:
    st.session_state.generated_password = ""

col1, col2 = st.columns([3,1])

with col1:
    password = st.text_input("Password", value=st.session_state.generated_password)

with col2:
    if st.button("Generate"):
        new_password = generate_password()
        st.session_state.generated_password = new_password
        pyperclip.copy(new_password)
        st.success("Password generated & copied!")

# Save Button
if st.button("Add"):
    if not website or not email or not password:
        st.warning("One or more fields are empty")
    else:
        save_data(website, email, password)
        st.success("Saved successfully!")
        st.session_state.generated_password = ""
