import tkinter
from json import JSONDecodeError
from tkinter import messagebox
import string
import random
import json

password_selection_list = string.ascii_letters + string.digits + string.punctuation

# ---------------------------- SEARCH FUNCTION ------------------------------- #
def search():
    website = website_entry.get()
    with open("data.json", "r") as data_file:
        try:
            data = json.load(data_file)
        except JSONDecodeError:
            messagebox.showinfo(message="No Password Stored")
            return
        else:
            try:
                website_data = data[website]
            except KeyError:
                messagebox.showinfo(message="Password for this\n"
                                            "Website is not stored")
                return
            else:
                email, password = website_data.items()
                messagebox.showinfo(title=f"{website}", message=f"Email: {email[1]}\n"
                                                                f"Password: {password[1]}")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, tkinter.END)
    length_password = random.randint(8, 12)
    password = ""
    for i in range(length_password):
        password += "".join(random.choice(password_selection_list))

    password_entry.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "Email": email,
            "Password": password
        }
    }
    if (len(website) == 0) or (len(email) == 0) or (len(password) == 0):
        messagebox.showinfo(message="A field was left empty\n"
                                    "Please fill all the fields")
        return

    save_or_not = messagebox.askokcancel(title=website, message="These are the Details Entered\n"
                                                       f"Email: {email}\n"
                                                       f"Password: {password}\n"
                                                       f"Is this Correct")

    if save_or_not:
        try:
            with open("data.json", "r") as data_file:
                try:
                    data = json.load(data_file)
                except JSONDecodeError:
                    data = {}
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        website_entry.delete(0, tkinter.END)
        email_entry.delete(0, tkinter.END)
        password_entry.delete(0, tkinter.END)
        website_entry.focus()
# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manger")
window.config(padx=50, pady=50)
window.minsize(width=400, height=300)

image_canvas = tkinter.Canvas(height=200, width=200)
logo_img = tkinter.PhotoImage(file="logo.png")
image_canvas.create_image(100, 100, image=logo_img)
image_canvas.grid(row=0, column=1)

#ALL the labels
website_label = tkinter.Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = tkinter.Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = tkinter.Label(text="Password:")
password_label.grid(row=3, column=0)

#ALL the entry boxes
website_entry = tkinter.Entry(width=26)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = tkinter.Entry(width=45)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = tkinter.Entry(width=26)
password_entry.grid(row=3, column=1)

#ALl the buttons
generate_password_button = tkinter.Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = tkinter.Button(text="ADD", width=37, command=add_password)
add_button.grid(row=4, column=1, columnspan=2)
search_button = tkinter.Button(text="Search", command=search, width=15)
search_button.grid(row=1, column=2)

window.mainloop()