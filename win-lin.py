"""
TODO:

    * Make MORE customizablity options.
    * Make Bold, Italic and Underline text.

"""

from tkinter import *
from tkinter import filedialog, messagebox, font
from PIL import Image, ImageTk
import tkmacosx
global save_delete_used
save_delete_used = True

root = Tk()
root.geometry("600x600")
root.minsize(height = 250, width = 250)
root.title("pyText")

light_main = "#ffffff"
light_alt0 = "#c3c3c3"
light_alt1 = "#1c1c1c"
light_text = "#000000" 
light_pallet = "themes/light/pallet.png"

dark_main = "#333333"
dark_alt0 = "#222222"
dark_alt1 = "#8c8c8c"
dark_text = "#ffffff"
dark_pallet = "themes/dark/pallet.png"

ct_option_current_option = StringVar(root)

with open("settings/theme/current_theme.txt") as theme_file:
    theme = theme_file.read()
    print(f"DEBUG --- Current theme is {theme}.")

if theme == "dark":
    ct_main = dark_main
    ct_alt0 = dark_alt0
    ct_alt1 = dark_alt1
    ct_text = dark_text
    ct_pallet = dark_pallet
elif theme == "light":
    ct_main = light_main
    ct_alt0 = light_alt0
    ct_alt1 = light_alt1
    ct_text = light_text
    ct_pallet = light_pallet
else:
    messagebox.showerror(title = "Error", message = "Please change the contents of 'current_theme.txt' in the directory 'settings/theme' to 'light'.")
    root.destroy()

with open("settings/theme/current_theme.txt") as theme_file:
    theme = theme_file.read()
    print(f"DEBUG --- Current theme is {theme}.")

with open("settings/theme/current_font.txt") as font_file:
    current_font = font_file.read()
    print(f"DEBUG --- Current font is {current_font}.")

root.config(bg = ct_main)

# Functions

def themes_page():
    def comfirm_theme():
        with open("settings/theme/current_theme.txt", "w") as theme_file:
            new_theme = f"{ct_option_current_option.get()}"
            theme_file.write(new_theme)
            messagebox.showinfo(title = "Completed", message = "Restart pyText to change the theme.")
    ct_option_options = ["light", "dark"]
    if theme in ct_option_options:
        ct_option_options.remove(theme)
    else:
        root.destroy()
    themes_frame = Frame(settings_display, bg = ct_main)
    Label(themes_frame, text = "Themes Settings", font = (current_font, 15), bg = ct_main, fg = ct_text).pack(side = TOP)

    # Theme

    ct_option = OptionMenu(themes_frame, ct_option_current_option, theme, *ct_option_options)
    ct_option.config(bg = ct_main, fg = ct_text)
    ct_option.pack(side = LEFT)
    ct_confirm = tkmacosx.Button(themes_frame, text = "Set Theme", command = comfirm_theme, borderless=1, bg = ct_alt1, font = (current_font, 12))
    ct_confirm.config(fg = ct_text)
    ct_confirm.config(bg = ct_main)
    ct_confirm.pack(side = RIGHT)
    themes_frame.pack(pady = 20)

def fonts_page():
    def confirm_font():
        with open("settings/theme/current_font.txt", "w") as font_file:
            new_font = f"{ct_option_current_option.get()}"
            font_file.write(new_font)
            messagebox.showinfo(title = "Completed", message = "Restart pyText to change the font.")
    ct_option_options = font.families()
    ct_list_options = []
    for fonterson in ct_option_options:
        ct_list_options.append(fonterson)
    ct_list_options.append("TkDefaultFont")
    fonts_frame = Frame(settings_display, bg = ct_main)
    Label(fonts_frame, text = "Fonts Settings", font = (current_font, 15), bg = ct_main, fg = ct_text).pack(side = TOP)
    
    ct_option = OptionMenu(fonts_frame, ct_option_current_option, current_font, *ct_list_options)
    ct_option.config(bg = ct_main, fg = ct_text)
    ct_option.pack(side = LEFT)
    ct_confirm = tkmacosx.Button(fonts_frame, text = "Set Font", command = confirm_font, borderless=1, bg = ct_alt1, font = (current_font, 12))
    ct_confirm.config(fg = ct_text)
    ct_confirm.config(bg = ct_main)
    ct_confirm.pack(side = RIGHT)
    fonts_frame.pack(pady = 20)

def hide_all_indicators():
    tib_indicator.config(bg = ct_alt0)

def hide_all_frames():
    for frame in settings_display.winfo_children():
        frame.destroy()

def show_indicator(indicator, page):
    hide_all_indicators()
    hide_all_frames()
    indicator.config(bg = ct_alt1)
    page()

def when_closing(event):
    when_X_clicked()

def when_X_clicked():
    if save_delete_used == False:
        messagebox.showwarning(title = "Save first!", message = "Save your document before closing pyText! If you would like to continue, use task manager to close.")
    else:
        close_pyText()

def settings_key(event):
    open_settings()

def open_settings():
    settings_menu = Toplevel(root)
    settings_menu.title("pyText Settings")
    settings_menu.geometry("500x300")
    settings_menu.resizable(False, False)

    # Images
    pallet_picture = Image.open(ct_pallet)
    pallet_png = ImageTk.PhotoImage(pallet_picture)

    # Side Nav

    settings_side_nav_frame = Frame(settings_menu, bg = ct_alt0)
    settings_side_nav_frame.pack(side = LEFT)
    settings_side_nav_frame.pack_propagate(False)
    settings_side_nav_frame.configure(width = 130, height = 300)

    Label(master = settings_menu,text = "Settings", bg = ct_alt0, font = (current_font, 25), fg = ct_text).place(x = 3, y = 0)

    themes_image_btn = tkmacosx.Button(settings_side_nav_frame, image = pallet_png, bg = ct_alt0, command = lambda: show_indicator(tib_indicator, themes_page), borderless=1, font = (current_font, 12))
    themes_image_btn.image = pallet_png
    themes_image_btn.place(x = 20, y = 50)

    fonts_image_btn = tkmacosx.Button(settings_side_nav_frame, image = pallet_png, bg = ct_alt0, command = lambda: show_indicator(tib_indicator, fonts_page), borderless=1, font = (current_font, 12))
    fonts_image_btn.image = pallet_png
    fonts_image_btn.place(x = 20, y = 100)

    global tib_indicator
    tib_indicator = Label(settings_side_nav_frame, text = " ", bg = ct_alt0)
    tib_indicator.place(x = 1, y = 50, width = 5, height = 40)

    global fib_indicator
    fib_indicator = Label(settings_side_nav_frame, text = " ", bg = ct_alt0)
    fib_indicator.place(x = 1, y = 100, width = 5, height = 40)

    # Main Screen

    global settings_display
    settings_display = Frame(settings_menu, bg = ct_main)
    settings_display.pack(side = LEFT)
    settings_display.pack_propagate(False)
    settings_display.configure(width = 400, height = 500)

def bolden_key(event):
    bolden_text()

def bolden_text():
    pass

def italic_key(event):
    italic_text()

def italic_text():
    pass

def underline_key(event):
    underline_text()

def underline_text():
    pass

def copy_key(event):
    copy_text()

def copy_text():
    text.event_generate("<<Copy>>")

def cut_key(event):
    cut_text()

def cut_text():
    text.event_generate("<<Cut>>")

def paste_key(event):
    paste_text()

def paste_text():
    text.event_generate("<<Paste>>")

def select_all_key(event):
    select_all_text()

def select_all_text():
    text.tag_add("sel", "1.0", END)

def on_text_change(event):
    global save_delete_used
    save_delete_used = False

def close_pyText():
    if save_delete_used == False:
        messagebox.showwarning(title = "Save first!", message = "Save your document before closing pyText! If you would like to continue, use task manager to close.")
    else:
        close_question = messagebox.askquestion(title = "Would you like to close pyText?", message = "Would you like to close pyText?", icon = "question")
        if close_question == "yes":
            root.quit()
        else:
            return

def opening_file_key(event):
    open_file()

def open_file():
    file_path = filedialog.askopenfilename()
    try:
        with open(file_path, "r") as file:
            text.insert("1.0", file.read())
            global save_path
            save_path = file_path
    except IsADirectoryError:
        messagebox.showerror(title = "Error", message = "You have selected a directory as your file, please try again")
        open_file()
    except:
        messagebox.showerror(title = "Error", message = "An unknown error occurred, please try again.")
        return

def saving_key(event):
    save_file()

def save_file():
    try:
        with open(save_path, "w") as file:
                file.write(text.get("1.0", END))
                global save_delete_used
                save_delete_used = True
    except:
        save_as_file()

def saving_as_key(event):
    save_as_file()

def save_as_file():
    global save_path
    save_path = filedialog.asksaveasfilename()
    try:
        with open(save_path, "w") as file:
            file.write(text.get("1.0", END))
            global save_delete_used
            save_delete_used = True
    except:
        messagebox.showerror(title = "Error", message = "An unknown error occurred, please try again.")
        return
    
def discard_key(event):
    discard_file()

def discard_file():
    discard_question = messagebox.askquestion(title = "Discard file?", message = "Are you sure that you want to discard this file? It will undo all changes create a new file.")
    if discard_question == "yes":
        global save_delete_used
        save_delete_used = True
        new_file()

def new_file_key(event):
    new_file()

def new_file():
    if save_delete_used == False:
        messagebox.showwarning(title = "Save first!", message = "Save your document before creating a new file!")
        new_file_question = messagebox.askquestion(title = "New file?", message = "Would you like to create a new file, discarding the one you're currently editing?", icon = "question")
        if new_file_question == "yes":
            text.delete("1.0", END)
        else:
            return
    else:
        text.delete("1.0", END)

# Basic text editor and scroll-bar

scroll_bar = Scrollbar(root)
scroll_bar.pack(side = RIGHT, fill = Y)

text = Text(root, yscrollcommand = scroll_bar.set, undo = True, bg = ct_main, fg = ct_text, font = (current_font, 15))
text.bind("<<Modified>>", on_text_change)
text.pack(fill = BOTH, expand = True)

scroll_bar.config(command = text.yview)

# Menu-bar

menu_bar = Menu(root)

file_menu = Menu(menu_bar, tearoff = False)
file_menu.add_command(label = "New", command = new_file, accelerator = "Ctrl+N")
file_menu.add_separator()
file_menu.add_command(label = "Open", command = open_file, accelerator = "Ctrl+O")
file_menu.add_separator()
file_menu.add_command(label = "Save", command = save_file, accelerator = "Ctrl+S")
file_menu.add_command(label = "Save As", command = save_as_file, accelerator = "Ctrl+S")
file_menu.add_separator()
file_menu.add_command(label = "Discard File", command = discard_file, accelerator = "Ctrl+D")
menu_bar.add_cascade(label = "File", menu = file_menu)

edit_menu = Menu(menu_bar, tearoff = False)
edit_menu.add_command(label = "Copy", command = copy_text, accelerator = "Ctrl+C")
edit_menu.add_command(label = "Cut", command = cut_text, accelerator = "Ctrl+X")
edit_menu.add_command(label = "Paste", command = paste_text, accelerator = "Ctrl+V")
edit_menu.add_separator()
edit_menu.add_command(label = "Select All", command = select_all_text, accelerator = "Ctrl+A")
menu_bar.add_cascade(label = "Edit", menu = edit_menu)

format_menu = Menu(menu_bar, tearoff = False)
format_menu.add_command(label = "Bolden Text", command = bolden_text, accelerator = "Ctrl+B")
format_menu.add_command(label = "Italic Text", command = italic_text, accelerator = "Ctrl+I")
format_menu.add_command(label = "Underline Text", command = underline_text, accelerator = "Ctrl+U")
menu_bar.add_cascade(label = "Format", menu = format_menu)

options_menu = Menu(menu_bar, tearoff = False)
options_menu.add_command(label = "pyText Setttings", command = open_settings, accelerator = "Ctrl+/")
options_menu.add_command(label = "Close pyText", command = close_pyText, accelerator = "Ctrl+W")
menu_bar.add_cascade(label = "Options", menu = options_menu)

# Keyboard Shortcuts

root.bind("<Control-n>", new_file_key)
root.bind("<Control-o>", opening_file_key)
root.bind("<Control-s>", saving_key)
root.bind("<Alt-s>", saving_as_key)
root.bind("<Control-d>", discard_key)
root.bind("<Control-b>", bolden_key)
root.bind("<Control-i>", italic_key)
root.bind("<Control-u>", underline_key)
root.bind("<Control-/>", settings_key)
root.bind("<Control-w>", when_closing)

root.protocol("WM_DELETE_WINDOW", when_X_clicked)
root.config(menu = menu_bar)

root.mainloop()