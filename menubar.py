from customtkinter import *
from CTkMenuBar import *

root = CTk()
root.title("pyText")
root.geometry("600x600")

def functioner1():
	print("meow 1")

def functioner2():
	print("meow 2")

menu = CTkMenuBar(master = root)
button = menu.add_cascade("Menu")

dropdown = CustomDropdownMenu(widget = button)
dropdown.add_option(option = "value 1", command = functioner1) 
dropdown.add_separator() 
submenu = dropdown.add_submenu("submenu") 
submenu.add_option(option = "value 2", command = functioner2)

root.mainloop()
