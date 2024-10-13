import tkinter
from tkinter import messagebox
import string
import random

password_selection_list = string.ascii_letters + string.digits + string.punctuation
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
    if (len(website) == 0) or (len(email) == 0) or (len(password) == 0):
        messagebox.showinfo(message="A field was left empty\n"
                                    "Please fill all the fields")
        return

    save_or_not = messagebox.askokcancel(title=website, message="These are the Details Entered\n"
                                                       f"Email: {email}\n"
                                                       f"Password: {password}\n"
                                                       f"Is this Correct")

    if save_or_not:
        with open("data.txt", "a") as file:
            file.write(f"{website} | {email} | {password}\n")
            file.close()

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
website_entry = tkinter.Entry(width=44)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = tkinter.Entry(width=44)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = tkinter.Entry(width=26)
password_entry.grid(row=3, column=1)

#ALl the buttons
generate_password_button = tkinter.Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = tkinter.Button(text="ADD", width=37, command=add_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()