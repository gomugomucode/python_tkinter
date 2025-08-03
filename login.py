from tkinter import *
from tkinter import messagebox
import bcrypt

def login():
    entered_email = emailfield.get().strip()
    entered_pw = passfield.get().strip()

    if not entered_email or not entered_pw:
        messagebox.showerror("Error", "Fill in all fields.")
        return

    try:
        with open("output.txt", "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        messagebox.showerror("Error", "No registrations found.")
        return

    stored_hash = None

    for i, line in enumerate(lines):
        if line.startswith("Email:"):
            file_email = line.split("Email:")[1].strip()
            if file_email == entered_email:
                hash_line = lines[i+2]  # Because: Plain Password, THEN Password Hash
                stored_hash = hash_line.split("Password Hash:")[1].strip()
                break

    if stored_hash is None:
        messagebox.showerror("Error", "Email not found.")
        return

    if bcrypt.checkpw(entered_pw.encode(), stored_hash.encode()):
        messagebox.showinfo("Success", "Login successful!")
    else:
        messagebox.showerror("Error", "Incorrect password.")

root = Tk()
root.title("Login Form")
root.geometry("400x300")
root.resizable(False, False)

# Frame for padding and alignment
form_frame = Frame(root, padx=30, pady=30)
form_frame.pack(fill=BOTH, expand=True)

# Heading
heading = Label(form_frame, text="Welcome Back! Please Login", font=("Arial", 16, "bold"))
heading.grid(row=0, column=0, columnspan=2, pady=(0, 25))

# Email
Label(form_frame, text="Email:", font=("Arial", 12)).grid(row=1, column=0, sticky=W, pady=8)
emailfield = Entry(form_frame, width=30, font=("Arial", 12))
emailfield.grid(row=1, column=1, pady=8)

# Password
Label(form_frame, text="Password:", font=("Arial", 12)).grid(row=2, column=0, sticky=W, pady=8)
passfield = Entry(form_frame, show="*", width=30, font=("Arial", 12))
passfield.grid(row=2, column=1, pady=8)

# Login Button
login_btn = Button(form_frame, text="Login", command=login,
                   bg="#007ACC", fg="white",
                   activebackground="#005F99", activeforeground="white",
                   font=("Arial", 12), width=20)
login_btn.grid(row=3, column=0, columnspan=2, pady=25)

# Set focus on email field
emailfield.focus()

root.mainloop()
