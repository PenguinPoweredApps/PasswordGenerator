# password_generator.py
# Author: Simon Wollerton, simon@penguinpowered.co.uk
""" A simple Python script to generate a user defined secure password.
    To ensure the greatest security select 32 charcaters along with uppercase,
    numbers and special characters. """

import random
import tkinter as tk
import tkinter.ttk as ttk
import pyperclip


def generate_password():

    password_text.delete("1.0", "end")
    password_length = password_length_variable.get()

    characters = list("abcdefghijklmnopqrstuvwxyz")

    if uppercase_char_choice.get() == 1:
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    if numbers_choice.get() == 1:
        characters.extend(list("0123456789"))

    if special_char_choice.get() == 1:
        characters.extend(list("!£$%^&*()-_+={}[]:;@~#<,>.?/"))

    length = int(password_length)

    the_password = "".join(random.choice(characters) for i in range(length))
    password_text.insert(tk.INSERT, the_password)
    status_label_value.set("Password generated successfully")


def copy_password():
    password = password_text.get("1.0", "end")
    pyperclip.copy(password)
    status_label_value.set("Password copied successfully")


root = tk.Tk()

root.title("My Password Generator")
root.iconphoto(True, tk.PhotoImage(file="padlock.png"))
root.geometry("660x300+300+300")
root.resizable(False, False)

# App title Label
title_label = tk.Label(
    root, text="Password Generator", font="Arial 16 bold", bg="brown", fg="#FF0"
)


# Application widgets
# Password length Label
password_length_label = tk.Label(root, text="Select a password length: ")


# Initial password length value
password_length_variable = tk.IntVar(value=6)
# Password length Spinbox
password_length_value = tk.Spinbox(
    root, textvariable=password_length_variable, from_=0, to=32, increment=1
)

uppercase_char_choice = tk.IntVar()
numbers_choice = tk.IntVar()
special_char_choice = tk.IntVar()


# Uppercase character selection Checkbutton
uppercase_character_checkbutton = tk.Checkbutton(
    root,
    text="Select to include uppercase characters: ",
    variable=uppercase_char_choice,
    offvalue=0,
    onvalue=1,
)
# Uppercase character example Label
uppercase_character_example_label = tk.Label(text="eg. ABCDEFGH...")


# Number selection Checkbutton
numbers_checkbutton = tk.Checkbutton(
    root,
    text="Select to include numbers: ",
    variable=numbers_choice,
    offvalue=0,
    onvalue=1,
)
# Number example Label
numbers_example_label = tk.Label(text="eg. 12345678...")


# Special character selection Checkbutton
special_characters_checkbutton = tk.Checkbutton(
    root,
    text="Select to include special characters: ",
    variable=special_char_choice,
    offvalue=0,
    onvalue=1,
)
# Special character example Label
special_characters_example_label = tk.Label(text="eg. !£$%^&*(...")


# Generated password Label
password_label = tk.Label(root, text="Your password is: ")
# Generated password appears here
password_text = tk.Text(root, height=1, width=32)
# Password Text box initial display blank
password_text_initial_value = ""
password_text.insert(tk.INSERT, password_text_initial_value)


# App Buttons
generate_button = ttk.Button(text="Generate", command=generate_password)
copy_button = ttk.Button(text="Copy", command=copy_password)
exit_button = ttk.Button(text="Exit", command=root.destroy)

# Status label
status_label_value = tk.StringVar()
status_label_value.set("App status info will appear here")
status_label = tk.Label(root, textvariable=status_label_value)

# Add all widgets to the root window with a Grid layout manager
title_label.grid(row=0, columnspan=3, padx=20, pady=20, sticky="ew")

password_length_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
password_length_value.grid(row=1, column=1, padx=5, pady=5, sticky="w")

uppercase_character_checkbutton.grid(row=2, column=0, padx=5, pady=5, sticky="w")
uppercase_character_example_label.grid(row=2, column=1, padx=5, pady=5, sticky="w")

numbers_checkbutton.grid(row=3, column=0, padx=5, pady=5, sticky="w")
numbers_example_label.grid(row=3, column=1, padx=5, pady=5, sticky="w")

special_characters_checkbutton.grid(row=4, column=0, padx=5, pady=5, sticky="w")
special_characters_example_label.grid(row=4, column=1, padx=5, pady=5, sticky="w")

password_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")
password_text.grid(row=5, column=1, padx=5, pady=5, sticky="w")

generate_button.grid(row=6, column=0, padx=5, pady=5, sticky="ew")
copy_button.grid(row=6, column=1, padx=5, pady=5, sticky="ew")
exit_button.grid(row=6, column=2, padx=5, pady=5, sticky="ew")

status_label.grid(row=7, columnspan=3, padx=5, pady=5, sticky="ew")

# Start the root window mainloop()
root.mainloop()
