from CTkColorPicker import *
from customtkinter import *

def turn_colour_into_var(pickedcolour):
    global colour
    colour = pickedcolour

def print_var():
    label.configure(text = f"Current colour output: {colour}")

root = CTk()

colour = "#ffffff"

def win_open():
    win = CTkToplevel()
    colourpicker = CTkColorPicker(win, width=500, command = lambda hex: turn_colour_into_var(hex))
    colourpicker.pack(padx=10, pady=10)

CTkButton(root, text = "open win", command = win_open).pack(pady = 10)

CTkButton(root, text = "print colour", command = print_var).pack()

label = CTkLabel(root, text = "Current colour output: None")
label.pack()

root.mainloop()