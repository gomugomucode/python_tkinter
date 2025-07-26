# from tkinter import *

# # Create the main window
# root = Tk()
# root.title("This is my first program")  # Set window title
# root.geometry("400x250")               # Set window size

# # # Create a StringVar to hold text for the label
# # text_var = StringVar()
# # text_var.set("This is the variable of label")  # Set the initial value

# # # Create a label that uses the text variable
# # label = Label(
# #     root,
# #     textvariable=text_var,   # Link the label to the StringVar
# #     anchor=CENTER,           # Center the text inside the label
# #     bg="blue",               # Set background color
# #     padx=15,                 # Add horizontal padding inside the label
# #     pady=15                  # Add vertical padding inside the label
# # )

# # button=Button(root,text="Click me",activebackground="blue",activeforeground="white",height=2,padx=20,pady=30)

# # # Place the label in the window with extra vertical spacing
# # label.pack(pady=20)

# # button.pack(padx=20,pady=40)

# # Start the Tkinter event loop
# root.mainloop()




from tkinter import *

from tkinter import messagebox  # Import for popup messages

def add_placeholder(entry, placeholder, is_password=False):
    def on_focus_in(event):
        if entry.get() == placeholder:
            entry.delete(0, END)
            entry.config(fg="black")
            if is_password:
                entry.config(show="*")
    
    def on_focus_out(event):
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.config(fg="grey")
            if is_password:
                entry.config(show="")

    entry.insert(0, placeholder)
    entry.config(fg="grey")
    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)


def submit():
    name = username_entry.get()
    password = password_entry.get()

    # Check if username or password is empty or still showing placeholder text
    if name == "" or name == "Enter your name":
        messagebox.showerror("Error", "Username is required.")
        return
    if password == "" or password == "Enter your password":
        messagebox.showerror("Error", "Password is required.")
        return
    
    print("The name is:", name)
    print("The password is:", password)
    
    # Clear fields and reset placeholders
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    add_placeholder(username_entry, "Enter your name")
    add_placeholder(password_entry, "Enter your password", is_password=True)

# Create main window
root = Tk()
root.title("Login Form")
root.geometry("400x200")

# Username label and entry
Label(root, text="Username").grid(row=0, column=0, padx=10, pady=10, sticky=E)
username_entry = Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=10)
add_placeholder(username_entry, "Enter your name")

# Password label and entry
Label(root, text="Password").grid(row=1, column=0, padx=10, pady=10, sticky=E)
password_entry = Entry(root)
password_entry.grid(row=1, column=1, padx=10, pady=10)
add_placeholder(password_entry, "Enter your password", is_password=True)

# Submit button
submit_button = Button(root, text="Submit", command=submit)
submit_button.grid(row=2, column=1, pady=20)

root.mainloop()
