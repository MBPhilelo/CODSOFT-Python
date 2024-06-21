from tkinter import *
import tkinter.messagebox as messagebox
import random, string

def passgen():
    if choice.get() == 1:
        return "".join(random.sample(poor, val.get()))
    elif choice.get() == 2:
        return "".join(random.sample(average, val.get()))
    elif choice.get() == 3:
        return "".join(random.sample(advance, val.get()))

def callback():
    generated_password = passgen()
    password_entry.delete(0, END)
    password_entry.insert(0, generated_password)
    messagebox.showinfo("Generated Password", f"Your generated password is: {generated_password}")

# Initialize main window
root = Tk()
root.geometry("400x400")
root.title("Password Generator")
root.configure(bg='#add8e6')  # Set background color

# Title label
title = Label(root, text="Password Generator", font=("Arial", 18, "bold"), bg='#add8e6')
title.pack(pady=10)

# Instruction label
instruction = Label(root, text="Choose the strength of the password:", font=("Arial", 12, "bold"), bg='#add8e6')
instruction.pack()

# Strength choice radio buttons
choice = IntVar()
R1 = Radiobutton(root, text="Weak", variable=choice, value=1, font=("Arial", 12), bg='#add8e6')
R2 = Radiobutton(root, text="Medium", variable=choice, value=2, font=("Arial", 12), bg='#add8e6')
R3 = Radiobutton(root, text="Strong", variable=choice, value=3, font=("Arial", 12), bg='#add8e6')
R1.pack(anchor=CENTER)
R2.pack(anchor=CENTER)
R3.pack(anchor=CENTER)

# Password length label
lenlabel = Label(root, text="Password Length", font=("Arial", 14, "bold"), bg='#add8e6')
lenlabel.pack(pady=10)

# Spinbox for password length
val = IntVar(value=8)
spinlength = Spinbox(root, from_=8, to_=24, textvariable=val, width=10, font=("Arial", 12))
spinlength.pack()

# Generate password button
passgenButton = Button(root, text="Generate", bd=3, command=callback, font=("Arial", 12))
passgenButton.pack(pady=20)

# Entry to display generated password
password_entry = Entry(root, font=("Arial", 12), width=30)
password_entry.pack(pady=10)

# Copy password button
copy_button = Button(root, text="Copy Password", bd=3, font=("Arial", 12), command=lambda: root.clipboard_append(password_entry.get()))
copy_button.pack(pady=10)

# Character sets for password generation
poor = string.ascii_uppercase + string.ascii_lowercase
average = string.ascii_uppercase + string.ascii_lowercase + string.digits
symbols = """`~!@#$%^&*()_-+={}[]|:;"'<>,.?/"""
advance = poor + average + symbols

# Run the main event loop
root.mainloop()
