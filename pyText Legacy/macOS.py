"""
TODO:

    * Make MORE customizablity options.
    * Make Bold, Italic and Underline text.

"""

from tkinter import *
from tkinter import filedialog, messagebox, font
from tkinter.font import Font
from PIL import Image, ImageTk
import tkmacosx
import webbrowser as web
import platform
global save_delete_used
save_delete_used = True

with open("settings/theme/current_theme.txt") as theme_file:
    theme = theme_file.read()
    print(f"DEBUG --- Current theme is {theme}.")

with open("settings/font/current_font.txt") as font_file:
    current_font = font_file.read()
    print(f"DEBUG --- Current font is {current_font}.")

with open("settings/font/current_font_size.txt") as font_file:
    current_font_size = font_file.read()
    print(f"DEBUG --- Current font size is {current_font_size}.")

with open("settings/theme/current_tab_size.txt") as tab_file:
    current_tab_size = tab_file.read()
    print(f"DEBUG --- Current tab size is {current_tab_size}.")

with open("settings/window/window_size.txt") as window_file:
    window_size = window_file.read()
    print(f"DEBUG --- Current window size is {window_size}.")

root = Tk()
if window_size == "Full Screen":
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    root.geometry(f"{screenwidth}x{screenheight}")
else:
    root.geometry(window_size)
root.minsize(height = 100, width = 100)
root.title("pyText")

light_main = "#ffffff"
light_alt0 = "#c3c3c3"
light_alt1 = "#1c1c1c"
light_text = "#000000" 
light_window = "themes/light/window.png"
light_font = "themes/light/font.png"

dark_main = "#333333"
dark_alt0 = "#222222"
dark_alt1 = "#8c8c8c"
dark_text = "#ffffff"
dark_window = "themes/dark/window.png"
dark_font = "themes/dark/font.png"

tab1 = " "
tab2 = "  "
tab3 = "   "
tab4 = "    "
tab5 = "     "
tab6 = "      "
tab7 = "       "
tab8 = "        "
tab9 = "         "
tab10 = "          "
tab11 = "           "
tab12 = "            "
tab13 = "             "
tab14 = "              "
tab15 = "               "

ct_option_current_option = StringVar(root)
ct_option_current_option1 = StringVar(root)
ct_option_current_option2 = StringVar(root)
ct_entry_current_option = StringVar(root)

operating_system = platform.system()

if theme == "dark":
    ct_main = dark_main
    ct_alt0 = dark_alt0
    ct_alt1 = dark_alt1
    ct_text = dark_text
    ct_window = dark_window
    ct_font = dark_font
elif theme == "light":
    ct_main = light_main
    ct_alt0 = light_alt0
    ct_alt1 = light_alt1
    ct_text = light_text
    ct_window = light_window
    ct_font = light_font
else:
    messagebox.showerror(title = "Error", message = "Please change the contents of 'current_theme.txt' in the directory 'settings/theme' to 'dark' or 'light'.")
    root.destroy()

root.config(bg = ct_main)

# Functions

def themes_page():
    def comfirm_theme():
        with open("settings/theme/current_theme.txt", "w") as theme_file:
            new_theme = f"{ct_option_current_option.get()}"
            theme_file.write(new_theme)
            messagebox.showinfo(title = "Completed", message = "Restart pyText to change the theme.")

    def confirm_tab_size():
        with open("settings/theme/current_tab_size.txt", "w") as tab_file:
            new_tab_size = f"{ct_option_current_option1.get()}"
            tab_file.write(new_tab_size)
            messagebox.showinfo(title = "Completed", message = "Restart pyText to change the tab size.")

    def confirm_window_size():
        with open("settings/window/window_size.txt", "w") as win_file:
            new_window_size = f"{ct_option_current_option2.get()}"
            win_file.write(new_window_size)
            messagebox.showinfo(title = "Completed", message = "Restart pyText to change the window size.")
        
    ct_option_options = ["light", "dark"]
    ct_option_options1 = []
    ct_option_options2 = ["100x100", "200x200", "300x300", "400x400", "500x500", "600x600", "700x700", "800x800", "900x900", "1000x1000", "Full Screen"]

    index = 1

    while index <= 15:
        ct_option_options1.append(index)
        index += 1

    print(ct_option_options1)

    if theme in ct_option_options:
        ct_option_options.remove(theme)
    else:
        root.destroy()

    themes_frame = Frame(settings_display, bg = ct_main)
    Label(themes_frame, text = "Window Settings", font = (current_font, 20), bg = ct_main, fg = ct_text).pack(side = TOP)

    # Theme

    Label(themes_frame, text = "Current Theme", font = (current_font, 15), bg = ct_main, fg = ct_text).pack(side = TOP)
    ct_option = OptionMenu(themes_frame, ct_option_current_option, theme, *ct_option_options)
    ct_option.config(bg = ct_main, fg = ct_text)
    ct_option.pack()
    ct_confirm = tkmacosx.Button(themes_frame, text = "Set Theme", command = comfirm_theme, borderless=1, font = (current_font, 15))
    ct_confirm.config(fg = ct_text)
    ct_confirm.config(bg = ct_alt1)
    ct_confirm.pack()

    # Tab Size

    Label(themes_frame, text = "Current Tab Size", font = (current_font, 15), bg = ct_main, fg = ct_text).pack(side = TOP)
    ct_option1 = OptionMenu(themes_frame, ct_option_current_option1, current_tab_size, *ct_option_options1)
    ct_option1.config(bg = ct_main, fg = ct_text)
    ct_option1.pack()
    ct_confirm1 = tkmacosx.Button(themes_frame, text = "Set Tab Size", command = confirm_tab_size, borderless=1, font = (current_font, 15))
    ct_confirm1.config(fg = ct_text)
    ct_confirm1.config(bg = ct_alt1)
    ct_confirm1.pack()

    # Window Size

    Label(themes_frame, text = "Current Window Size", font = (current_font, 15), bg = ct_main, fg = ct_text).pack(side = TOP)
    ct_option1 = OptionMenu(themes_frame, ct_option_current_option2, current_tab_size, *ct_option_options2)
    ct_option1.config(bg = ct_main, fg = ct_text)
    ct_option1.pack()
    ct_confirm1 = tkmacosx.Button(themes_frame, text = "Set Window Size", command = confirm_window_size, borderless=1, font = (current_font, 15))
    ct_confirm1.config(fg = ct_text)
    ct_confirm1.config(bg = ct_alt1)
    ct_confirm1.pack()

    themes_frame.pack(pady = 20)

def fonts_page():
    def confirm_font():
        with open("settings/font/current_font.txt", "w") as font_file:
            new_font = f"{ct_option_current_option.get()}"
            font_file.write(new_font)
            messagebox.showinfo(title = "Completed", message = "Restart pyText to change the font.")
    def confirm_font_size():
        with open("settings/font/current_font_size.txt", "w") as font_file:
            new_font_size = f"{ct_entry.get()}"
            font_file.write(new_font_size)
            messagebox.showinfo(title = "Completed", message = "Restart pyText to change the font size.")
    ct_option_options = font.families()
    ct_list_options = []
    for fonterson in ct_option_options:
        ct_list_options.append(fonterson)
    ct_list_options.append("TkDefaultFont")
    fonts_frame = Frame(settings_display, bg = ct_main)
    Label(fonts_frame, text = "Fonts Settings", font = (current_font, 20), bg = ct_main, fg = ct_text).pack(side = TOP)
    
    # Font Selection
    Label(fonts_frame, text = "Font", font = (current_font, 15), bg = ct_main, fg = ct_text).pack()
    ct_option = OptionMenu(fonts_frame, ct_option_current_option, current_font, *ct_list_options)
    ct_option.config(bg = ct_main, fg = ct_text)
    ct_option.pack()
    ct_confirm = tkmacosx.Button(fonts_frame, text = "Set Font", command = confirm_font, borderless = 1, bg = ct_alt1, font = (current_font, 15))
    ct_confirm.config(fg = ct_text)
    ct_confirm.pack()

    # Font Size
    Label(fonts_frame, text = "Font Size", font = (current_font, 15), bg = ct_main, fg = ct_text).pack()
    Label(fonts_frame, text = "(Only changes font-size in the editor)", font = (current_font, 10), bg = ct_main, fg = ct_text).pack()
    ct_entry = Entry(fonts_frame)
    ct_entry.config(bg = ct_alt1, fg = ct_text, font = (current_font, 15))
    ct_entry.pack()
    ct_confirm1 = tkmacosx.Button(fonts_frame, text = "Set Font Size", command = confirm_font_size, borderless = 1, bg = ct_alt1, font = (current_font, 15))
    ct_confirm1.config(fg = ct_text)
    ct_confirm1.pack()
    
    fonts_frame.pack(pady = 20)

def hide_all_frames(page):
    for frame in settings_display.winfo_children():
        frame.destroy()
    page()

def when_closing(event):
    when_X_clicked()

def when_X_clicked():
    if save_delete_used == False:
        messagebox.showwarning(title = "Save first!", message = "Save your document before closing pyText! If you would like to continue, press 'Command+Q'.")
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
    window_picture = Image.open(ct_window)
    window_png = ImageTk.PhotoImage(window_picture)
    font_picture = Image.open(ct_font)
    font_png = ImageTk.PhotoImage(font_picture)

    # Side Nav

    settings_side_nav_frame = Frame(settings_menu, bg = ct_alt0)
    settings_side_nav_frame.pack(side = LEFT)
    settings_side_nav_frame.pack_propagate(False)
    settings_side_nav_frame.configure(width = 130, height = 300)

    Label(master = settings_menu,text = "Settings", bg = ct_alt0, font = (current_font, 25), fg = ct_text).place(x = 3, y = 0)

    themes_image_btn = tkmacosx.Button(settings_side_nav_frame, image = window_png, bg = ct_alt0, command = lambda: hide_all_frames(themes_page), borderless=1, font = (current_font, 12))
    themes_image_btn.image = window_png
    themes_image_btn.place(x = 20, y = 50)

    fonts_image_btn = tkmacosx.Button(settings_side_nav_frame, image = font_png, bg = ct_alt0, command = lambda: hide_all_frames(fonts_page), borderless=1, font = (current_font, 12))
    fonts_image_btn.image = font_png
    fonts_image_btn.place(x = 20, y = 100)

    # Main Screen

    global settings_display
    settings_display = Frame(settings_menu, bg = ct_main)
    settings_display.pack(side = LEFT, fill = BOTH)
    settings_display.pack_propagate(False)
    settings_display.configure(width = 400, height = 500)


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
        messagebox.showwarning(title = "Save first!", message = "Save your document before closing pyText! If you would like to continue, press 'Command+Q'.")
    else:
        close_question = messagebox.askquestion(title = "Would you like to close pyText?", message = "Would you like to close pyText?", icon = "question")
        if close_question == "yes":
            root.quit()
        else:
            return

def opening_file_key(event):
    open_file()

def open_file():
    global file_path
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

def open_source():
    web.open("https://github.com/therealzakie/pyText", new = 2)

def open_source_key(event):
    open_source()

def open_readme():
    web.open("https://github.com/therealzakie/pyText/blob/master/README.md", new = 2)

def open_df_closing_safety():
    web.open("https://github.com/therealzakie/pyText/blob/master/documentation/features/closingsafety.md", new = 2)

def open_df_themes():
    web.open("https://github.com/therealzakie/pyText/blob/master/documentation/features/themes.md", new = 2)

def open_df_fonts():
    web.open("https://github.com/therealzakie/pyText/blob/master/documentation/features/font.md", new = 2)

def open_keybinds():
    web.open("https://github.com/therealzakie/pyText/blob/master/documentation/keybinds/keybinds_mac.md", new = 2)

# Basic text editor and scroll-bar

scroll_bar = Scrollbar(root)
scroll_bar.pack(side = RIGHT, fill = Y)

text = Text(root, yscrollcommand = scroll_bar.set, undo = True, bg = ct_main, fg = ct_text, font = (current_font, current_font_size))
text.bind("<<Modified>>", on_text_change)
fonter = Font(font=text['font'])
if current_tab_size == "1":
    tab = fonter.measure(tab1)
elif current_tab_size == "2":
    tab = fonter.measure(tab2)
elif current_tab_size == "3":
    tab = fonter.measure(tab3)
elif current_tab_size == "4":
    tab = fonter.measure(tab4)
elif current_tab_size == "5":
    tab = fonter.measure(tab5)
elif current_tab_size == "6":
    tab = fonter.measure(tab6)
elif current_tab_size == "7":
    tab = fonter.measure(tab7)
elif current_tab_size == "8":
    tab = fonter.measure(tab8)
elif current_tab_size == "9":
    tab = fonter.measure(tab9)
elif current_tab_size == "10":
    tab = fonter.measure(tab10)
elif current_font_size == "11":
    tab = fonter.measure(tab11)
elif current_tab_size == "12":
    tab = fonter.measure(tab12)
elif current_tab_size == "13":
    tab = fonter.measure(tab13)
elif current_tab_size == "14":
    tab = fonter.measure(tab14)
elif current_tab_size == "15":
    tab = fonter.measure(tab15)
else:
    root.destroy()
text.config(tabs = tab)
text.pack(fill = BOTH, expand = True)

scroll_bar.config(command = text.yview)

# Menu-bar

menu_bar = Menu(root)

file_menu = Menu(menu_bar, tearoff = False)
file_menu.add_command(label = "New", command = new_file, accelerator = "Cmd+N")
file_menu.add_separator()
file_menu.add_command(label = "Open", command = open_file, accelerator = "Cmd+O")
file_menu.add_separator()
file_menu.add_command(label = "Save", command = save_file, accelerator = "Cmd+S")
file_menu.add_command(label = "Save As", command = save_as_file, accelerator = "Ctrl+S")
file_menu.add_separator()
file_menu.add_command(label = "Discard File", command = discard_file, accelerator = "Cmd+D")
menu_bar.add_cascade(label = "File", menu = file_menu)

edit_menu = Menu(menu_bar, tearoff = False)
edit_menu.add_command(label = "Copy", command = copy_text, accelerator = "Cmd+C")
edit_menu.add_command(label = "Cut", command = cut_text, accelerator = "Cmd+X")
edit_menu.add_command(label = "Paste", command = paste_text, accelerator = "Cmd+V")
edit_menu.add_separator()
edit_menu.add_command(label = "Select All", command = select_all_text, accelerator = "Cmd+A")
menu_bar.add_cascade(label = "Edit", menu = edit_menu)

docs_menu = Menu(menu_bar, tearoff = False)
docs_menu.add_command(label = "Source Code", command = open_source, accelerator = "Cmd+G")
docs_menu.add_command(label = "READ ME", command = open_readme)
docs_menu.add_separator()
docs_features_menu = Menu(docs_menu, tearoff = False)
docs_features_menu.add_command(label = "Closing Safety", command = open_df_closing_safety)
docs_features_menu.add_command(label = "Themes", command = open_df_themes)
docs_features_menu.add_command(label = "Fonts", command = open_df_fonts)
docs_menu.add_cascade(label = "Features", menu = docs_features_menu)
docs_menu.add_separator()
docs_menu.add_command(label = "Keybinds", command = open_keybinds)
menu_bar.add_cascade(label = "Documentation", menu = docs_menu)

options_menu = Menu(menu_bar, tearoff = False)
options_menu.add_command(label = "pyText Setttings", command = open_settings, accelerator = "Cmd+/")
options_menu.add_command(label = "Close pyText", command = close_pyText, accelerator = "Cmd+W")
menu_bar.add_cascade(label = "Options", menu = options_menu)

# Keyboard Shortcuts

root.bind("<Command-n>", new_file_key)
root.bind("<Command-o>", opening_file_key)
root.bind("<Command-s>", saving_key)
root.bind("<Control-s>", saving_as_key)
root.bind("<Command-d>", discard_key)
root.bind("<Command-g>", open_source_key)
root.bind("<Command-/>", settings_key)
root.bind("<Command-w>", when_closing)

root.protocol("WM_DELETE_WINDOW", when_X_clicked)
root.config(menu = menu_bar)

root.mainloop()