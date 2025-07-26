from tkinter import *
from tkinter import messagebox
import bcrypt

def submit(event=None):
    fname = fnamefield.get().strip()
    lname = lnamefield.get().strip()
    email = emailfield.get().strip()
    password = passfield.get().strip()
    gender = gender_var.get()
    agree = terms_var.get()

    if not fname or not lname or not email or not password:
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    if not agree:
        messagebox.showwarning("Agreement", "You must agree to the terms and conditions.")
        return

    full_name = f"{fname} {lname}"

    # --- Hash the password ---
    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    output = (
        f"Name: {full_name}\n"
        f"Email: {email}\n"
        f"Gender: {gender}\n"
        f"Plain Password: {password}\n"
        f"Password Hash: {hashed_pw.decode('utf-8')}\n"
        f"{'-'*40}\n"
    )

    print(output)

    with open("output.txt", "a") as f:
        f.write(output)

    messagebox.showinfo("Success", "Registration saved!")

    # Clear fields
    fnamefield.delete(0, END)
    lnamefield.delete(0, END)
    emailfield.delete(0, END)
    passfield.delete(0, END)
    terms_var.set(False)
    gender_var.set("Male")
    fnamefield.focus()

root = Tk()
root.title("Secure Registration Form")
root.geometry("400x400")
root.resizable(False, False)

form_frame = Frame(root, padx=20, pady=20)
form_frame.pack(fill=BOTH, expand=True)

heading = Label(form_frame, text="Register Securely", font=("Arial", 16, "bold"))
heading.grid(row=0, column=0, columnspan=2, pady=(0, 20))

Label(form_frame, text="First Name").grid(row=1, column=0, padx=10, pady=5, sticky=W)
fnamefield = Entry(form_frame, width=30)
fnamefield.grid(row=1, column=1, pady=5)

Label(form_frame, text="Last Name").grid(row=2, column=0, padx=10, pady=5, sticky=W)
lnamefield = Entry(form_frame, width=30)
lnamefield.grid(row=2, column=1, pady=5)

Label(form_frame, text="Email").grid(row=3, column=0, padx=10, pady=5, sticky=W)
emailfield = Entry(form_frame, width=30)
emailfield.grid(row=3, column=1, pady=5)

Label(form_frame, text="Password").grid(row=4, column=0, padx=10, pady=5, sticky=W)
passfield = Entry(form_frame, show="*", width=30)
passfield.grid(row=4, column=1, pady=5)

Label(form_frame, text="Gender").grid(row=5, column=0, padx=10, pady=5, sticky=W)
gender_var = StringVar(value="Male")
Radiobutton(form_frame, text="Male", variable=gender_var, value="Male").grid(row=5, column=1, sticky=W)
Radiobutton(form_frame, text="Female", variable=gender_var, value="Female").grid(row=5, column=1)

terms_var = BooleanVar()
terms_cb = Checkbutton(form_frame, text="I agree to the Terms and Conditions", variable=terms_var)
terms_cb.grid(row=6, columnspan=2, pady=10)

button = Button(form_frame, text="Register Securely", bg="blue", fg="white",
                activebackground="navy", activeforeground="white",
                width=20, command=submit)
button.grid(row=7, columnspan=2, pady=10)

root.bind("<Return>", submit)
fnamefield.focus()
root.mainloop()
