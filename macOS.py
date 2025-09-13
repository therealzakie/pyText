from customtkinter import *
from CTkMessagebox import *
from tkinter import filedialog, Menu, font, TkVersion
import webbrowser as web
import platform
import sys

global save_delete_used
save_delete_used = True

with open("settings/theme/current_theme.txt") as theme_file:
    theme = theme_file.read()
    print(f"DEBUG --- Current theme is {theme}.")

with open("settings/font/current_font.txt") as font_file:
    current_font = font_file.read()
    print(f"DEBUG --- Current font is {current_font}.")

with open("settings/font/current_font_size.txt") as font_file:
    current_font_size = float(font_file.read())
    print(f"DEBUG --- Current font size is {current_font_size}.")

with open("settings/theme/current_tab_size.txt") as tab_file:
    current_tab_size = tab_file.read()
    print(f"DEBUG --- Current tab size is {current_tab_size}.")

with open("settings/window/window_size.txt") as window_file:
    window_size = window_file.read()
    print(f"DEBUG --- Current window size is {window_size}.")

root = CTk()
if window_size == "Full Screen":
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    root.geometry(f"{screenwidth}x{screenheight}")
else:
    root.geometry(window_size)
root.minsize(height = 100, width = 100)
root.title("pyText")

light_window = "themes/light/window.png"
light_font = "themes/light/font.png"

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

pyText_version = "1.0 customtkinter build"

if theme == "dark":
    root._set_appearance_mode("dark")
    ct_window = dark_window
    ct_font = dark_font
elif theme == "light":
    root._set_appearance_mode("light")
    ct_window = light_window
    ct_font = light_font
else:
    root._set_appearance_mode("System")

# Functions

def when_closing(event):
    when_X_clicked()

def when_X_clicked():
    if save_delete_used == False:
        CTkMessagebox(title = "Save first!", message = "Save your document before closing pyText! If you would like to continue, press 'Command+D' and then close pyText.")
    else:
        close_pyText()

def settings_key(event):
    open_settings()

def open_settings():
    def confirm_theme():
        with open("settings/theme/current_theme.txt", "w") as theme_file:
            new_theme = f"{theme_option.get()}"
            theme_file.write(new_theme)
            CTkMessagebox(title = "Completed", message = "Make sure to change your system's theme in it's settings!")
            CTkMessagebox(title = "Completed", message = "Restart pyText to change the theme.")

    def confirm_tab_size():
        with open("settings/theme/current_tab_size.txt", "w") as tab_file:
            new_tab_size = f"{tab_size_option.get()}"
            tab_file.write(new_tab_size)
            CTkMessagebox(title = "Completed", message = "Restart pyText to change the tab size.")

    def confirm_window_size():
        with open("settings/window/window_size.txt", "w") as win_file:
            new_window_size = f"{window_size_option.get()}"
            win_file.write(new_window_size)
            CTkMessagebox(title = "Completed", message = "Restart pyText to change the window size.")
    
    def confirm_font():
            with open("settings/font/current_font.txt", "w") as font_file:
                new_font = f"{font_option.get()}"
                font_file.write(new_font)
                CTkMessagebox(title = "Completed", message = "Restart pyText to change the font.")
    def confirm_font_size():
        with open("settings/font/current_font_size.txt", "w") as font_file:
            new_font_size = f"{font_size_entry.get()}"
            font_file.write(new_font_size)
            CTkMessagebox(title = "Completed", message = "Restart pyText to change the font size.")

    theme_option = StringVar(root)
    tab_size_option = StringVar(root)
    window_size_option = StringVar(root)
    font_option = StringVar(root)

    settings = CTkToplevel(root)
    settings.geometry("500x500")
    settings.title("pyText Settings")
    settings.resizable(False, False)

    tabview = CTkTabview(settings, width = 460, height = 460)
    tabview.pack()
    tabview.add("Window")
    tabview.add("Font")
    tabview.add("Debug")

    # Options

    theme_options = ["light", "dark"]
    ctk_default_font = tuple(["CTkFont"])
    font_options = font.families() + ctk_default_font
    print(font_options)
    window_size_options = ["100x100", "200x200", "300x300", "400x400", "500x500", "600x600", "700x700", "800x800", "900x900", "1000x1000", "Full Screen"]
    tab_size_options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]

    # Window

    CTkLabel(tabview.tab("Window"), text = "Window Settings", font = (current_font, 20)).pack(side = TOP)
    
    window_frame = CTkScrollableFrame(tabview.tab("Window"), width = 400, height = 350)
    if theme == "dark":
        window_frame.configure(fg_color = "#252525")
    elif theme == "light":
        window_frame.configure(fg_color = "#FFFFFF")
    else:
        window_frame.configure(fg_color = "#6B6B6B")
    window_frame.pack()

    CTkLabel(window_frame, text = "Theme", font = (current_font, 15)).pack()
    theme_optionmenu = CTkOptionMenu(master = window_frame, values = theme_options, variable = theme_option)
    theme_optionmenu.set(theme)
    theme_optionmenu.pack()
    CTkLabel(window_frame, text = " ", font = (current_font, 3)).pack()
    CTkButton(window_frame, text = "Confirm", command = confirm_theme).pack()

    CTkLabel(window_frame, text = "Tab Size", font = (current_font, 15)).pack()
    tab_size_optionmenu = CTkOptionMenu(master = window_frame, values = tab_size_options, variable = tab_size_option)
    tab_size_optionmenu.set(current_tab_size)
    tab_size_optionmenu.pack()
    CTkLabel(window_frame, text = " ", font = (current_font, 3)).pack()
    CTkButton(window_frame, text = "Confirm", command = confirm_tab_size).pack()

    CTkLabel(window_frame, text = "Default Window Size", font = (current_font, 15)).pack()
    window_size_optionmenu = CTkOptionMenu(master = window_frame, values = window_size_options, variable = window_size_option)
    window_size_optionmenu.set(window_size)
    window_size_optionmenu.pack()
    CTkLabel(window_frame, text = " ", font = (current_font, 3)).pack()
    CTkButton(window_frame, text = "Confirm", command = confirm_window_size).pack()

    # Font

    CTkLabel(tabview.tab("Font"), text = "Font Settings", font = (current_font, 20)).pack(side = TOP)
    
    font_frame = CTkScrollableFrame(tabview.tab("Font"), width = 400, height = 350)
    if theme == "dark":
        font_frame.configure(fg_color = "#252525")
    elif theme == "light":
        font_frame.configure(fg_color = "#FFFFFF")
    else:
        font_frame.configure(fg_color = "#6B6B6B")
    font_frame.pack()

    CTkLabel(font_frame, text = "Font", font = (current_font, 15)).pack()

    font_optionmenu = CTkOptionMenu(master = font_frame, values = font_options, variable = font_option)
    font_optionmenu.set(current_font)
    font_optionmenu.pack()
    CTkLabel(font_frame, text = " ", font = (current_font, 3)).pack()
    CTkButton(font_frame, text = "Confirm", command = confirm_font).pack()

    CTkLabel(font_frame, text = "Font Size", font = (current_font, 15)).pack()

    font_size_entry = CTkEntry(master = font_frame, placeholder_text = "Font Size (Integer)")
    font_size_entry.pack()
    CTkLabel(font_frame, text = " ", font = (current_font, 3)).pack()
    CTkButton(font_frame, text = "Confirm", command = confirm_font_size).pack()

    # Debug Info

    CTkLabel(tabview.tab("Debug"), text = "Debug Information", font = (current_font, 20)).pack()
    
    debug_frame = CTkScrollableFrame(tabview.tab("Debug"), width = 400, height = 350)
    if theme == "dark":
        debug_frame.configure(fg_color = "#252525")
    elif theme == "light":
        debug_frame.configure(fg_color = "#A0A0A0")
    else:
        debug_frame.configure(fg_color = "#6B6B6B")
    debug_frame.pack()

    CTkLabel(debug_frame, text = f"Operating System: {platform.system()}").pack()
    CTkLabel(debug_frame, text = f"{platform.system()} Version: {platform.version()}").pack()
    CTkLabel(debug_frame, text = f"Python Version: {platform.python_version()}").pack()
    CTkLabel(debug_frame, text = f"pyText Version: {pyText_version}").pack()
    CTkLabel(debug_frame, text = f"customtkinter Module Version: {sys.modules['customtkinter'].__version__}").pack()
    CTkLabel(debug_frame, text = f"CTkMessagebox Module Version: {sys.modules['CTkMessagebox'].__version__}").pack()
    CTkLabel(debug_frame, text = f"tkinter Module Version: {TkVersion}").pack()

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
        CTkMessagebox(title = "Save first!", message = "Save your document before closing pyText! If you would like to continue, press 'Command+D' and then close pyText.")
    else:
        close_question = CTkMessagebox(title = "Would you like to close pyText?", message = "Would you like to close pyText?", icon="question", option_1="Cancel", option_2="No", option_3="Yes")
        if close_question.get() == "Yes":
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
        CTkMessagebox(title = "Error", message = "You have selected a directory as your file, please try again")
        open_file()
    except:
        CTkMessagebox(title = "Error", message = "An unknown error occurred, please try again.")
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
        CTkMessagebox(title = "Error", message = "An unknown error occurred, please try again.")
        return
    
def discard_key(event):
    discard_file()

def discard_file():
    discard_question = CTkMessagebox(title = "Discard file?", message = "Are you sure that you want to discard this file? It will undo all changes create a new file.", icon="question", option_1="Cancel", option_2="No", option_3="Yes")
    if discard_question.get() == "Yes":
        global save_delete_used
        save_delete_used = True
        new_file()

def new_file_key(event):
    new_file()

def new_file():
    if save_delete_used == False:
        CTkMessagebox(title = "Save first!", message = "Save your document before creating a new file!")
        new_file_question = CTkMessagebox(title = "New file?", message = "Would you like to create a new file, discarding the one you're currently editing?", icon="question", option_1="Cancel", option_2="No", option_3="Yes")
        if new_file_question.get() == "Yes":
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
    web.open("https://github.com/therealzakie/pyText/blob/master/documentation/keybinds/keybinds_windows_linux.md", new = 2)

# Basic text editor and scroll-bar

scroll_bar = CTkScrollbar(root)
scroll_bar.pack(side = RIGHT, fill = Y)

text = CTkTextbox(root, yscrollcommand = scroll_bar.set, undo = True, font = (current_font, current_font_size))
text.bind("<<Modified>>", on_text_change)
fonter = CTkFont()
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
text.configure(tabs = tab)
text.pack(fill = BOTH, expand = True)

scroll_bar.configure(command = text.yview)

# Menu Bar

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

docs_features_menu = Menu(docs_menu, tearoff = False)
docs_features_menu.add_command(label = "Closing Safety", command = open_df_closing_safety)
docs_features_menu.add_command(label = "Themes", command = open_df_themes)
docs_features_menu.add_command(label = "Fonts", command = open_df_fonts)
docs_menu.add_cascade(label = "Features", menu = docs_features_menu)
docs_menu.add_command(label = "Keybinds", command = open_keybinds)
menu_bar.add_cascade(label = "Documentation", menu = docs_menu)

options_menu = Menu(menu_bar, tearoff = False)
options_menu.add_command(label = "pyText Settings", command = open_settings, accelerator = "Cmd+/")
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