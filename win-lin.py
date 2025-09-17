from customtkinter import *
from CTkMessagebox import *
from tkinter import filedialog, font, TkVersion
import webbrowser as web
import platform
import sys
from CTkMenuBar import *

global save_delete_used
save_delete_used = True

root = CTk()

with open("settings/theme/current_theme.txt") as theme_file:
    theme = theme_file.read()
    print(f"DEBUG --- Current theme is {theme}.")

with open("settings/theme/current_colour_scheme.txt") as colour_file:
    colour_scheme = colour_file.read()
    set_default_color_theme(colour_scheme)
    print(f"DEBUG --- Current Colour Scheme is {colour_scheme}.")

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

pyText_version = "1.0.0 customtkinter build"

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
        CTkMessagebox(title = "Save first!", message = "Save your document before closing pyText! If you would like to continue, press 'Control+D' and then close pyText.")
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

    def confirm_colour_scheme():
        with open("settings/theme/current_colour_scheme.txt", "w") as colour_file:
            new_colour_scheme = f"{colour_option.get()}"
            colour_file.write(new_colour_scheme)
            CTkMessagebox(title = "Completed", message = "Restart pyText to change the colour scheme.")

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
    colour_option = StringVar(root)
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
    colour_options = ["blue", "dark_blue", "green"]
    ctk_default_font = tuple(["CTkFont"])
    font_options = font.families() + ctk_default_font
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

    CTkLabel(window_frame, text = "Colour Scheme", font = (current_font, 15)).pack()
    colour_optionmenu = CTkOptionMenu(master = window_frame, values = colour_options, variable = colour_option)
    colour_optionmenu.set(colour_scheme)
    colour_optionmenu.pack()
    CTkLabel(window_frame, text = " ", font = (current_font, 3)).pack()
    CTkButton(window_frame, text = "Confirm", command = confirm_colour_scheme).pack()

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
    CTkLabel(debug_frame, text = f"CTkMenuBar Module Version: {sys.modules['CTkMenuBar'].__version__}").pack()

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
        CTkMessagebox(title = "Save first!", message = "Save your document before closing pyText! If you would like to continue, press 'Control+D' and then close pyText.")
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

# MenuBar

if platform.system() == "Windows":
    menu = CTkTitleMenu(master = root)

    file_btn = menu.add_cascade("File")
    file_dropdown = CustomDropdownMenu(widget = file_btn)
    file_dropdown.add_option(option = "New (Ctrl+N)", command = new_file)
    file_dropdown.add_separator()
    file_dropdown.add_option(option = "Open (Ctrl+O)", command = open_file)
    file_dropdown.add_separator()
    file_dropdown.add_option(option = "Save (Ctrl+S)", command = save_file)
    file_dropdown.add_option(option = "Save as (Alt+S)", command = save_as_file)
    file_dropdown.add_option(option = "Discard File (Ctrl+D)", command = discard_file)

    edit_btn = menu.add_cascade("Edit")
    edit_dropdown = CustomDropdownMenu(widget = edit_btn)
    edit_dropdown.add_option(option = "Copy (Ctrl+C)", command = copy_text)
    edit_dropdown.add_option(option = "Cut (Ctrl+X)", command = cut_text)
    edit_dropdown.add_option(option = "Paste (Ctrl+V)", command = paste_text)
    edit_dropdown.add_separator()
    edit_dropdown.add_option(option = "Select All (Ctrl+A)", command = select_all_text)

    docs_btn = menu.add_cascade("Documentation")
    docs_dropdown = CustomDropdownMenu(widget = docs_btn)
    docs_dropdown.add_option(option = "Source Code (Ctrl+G)", command = open_source)
    docs_dropdown.add_option(option = "README", command = open_readme)
    docs_dropdown.add_separator()
    features_submenu = docs_dropdown.add_submenu("Features")
    features_submenu.add_option(option = "Closing Safety", command = open_df_closing_safety)
    features_submenu.add_option(option = "Editable Theme", command = open_df_themes)
    features_submenu.add_option(option = "Editable Font", command = open_df_fonts)
    docs_dropdown.add_option(option = "Keybinds", command = open_keybinds)

    options_btn = menu.add_cascade("Options")
    options_dropdown = CustomDropdownMenu(widget = options_btn)
    options_dropdown.add_option(option = "Settings (Ctrl+,)", command = open_settings)
    options_dropdown.add_option(option = "Close pyText (Ctrl+W)", command = close_pyText)

else:
    menu = CTkMenuBar(master = root)

    file_btn = menu.add_cascade("File")
    file_dropdown = CustomDropdownMenu(widget = file_btn)
    file_dropdown.add_option(option = "New (Ctrl+N)", command = new_file)
    file_dropdown.add_separator()
    file_dropdown.add_option(option = "Open (Ctrl+O)", command = open_file)
    file_dropdown.add_separator()
    file_dropdown.add_option(option = "Save (Ctrl+S)", command = save_file)
    file_dropdown.add_option(option = "Save as (Alt+S)", command = save_as_file)
    file_dropdown.add_option(option = "Discard File (Ctrl+D)", command = discard_file)

    edit_btn = menu.add_cascade("Edit")
    edit_dropdown = CustomDropdownMenu(widget = edit_btn)
    edit_dropdown.add_option(option = "Copy (Ctrl+C)", command = copy_text)
    edit_dropdown.add_option(option = "Cut (Ctrl+X)", command = cut_text)
    edit_dropdown.add_option(option = "Paste (Ctrl+V)", command = paste_text)
    edit_dropdown.add_separator()
    edit_dropdown.add_option(option = "Select All (Ctrl+A)", command = select_all_text)

    docs_btn = menu.add_cascade("Documentation")
    docs_dropdown = CustomDropdownMenu(widget = docs_btn)
    docs_dropdown.add_option(option = "Source Code (Ctrl+G)", command = open_source)
    docs_dropdown.add_option(option = "README", command = open_readme)
    docs_dropdown.add_separator()
    features_submenu = docs_dropdown.add_submenu("Features")
    features_submenu.add_option(option = "Closing Safety", command = open_df_closing_safety)
    features_submenu.add_option(option = "Editable Theme", command = open_df_themes)
    features_submenu.add_option(option = "Editable Font", command = open_df_fonts)
    docs_dropdown.add_option(option = "Keybinds", command = open_keybinds)

    options_btn = menu.add_cascade("Options")
    options_dropdown = CustomDropdownMenu(widget = options_btn)
    options_dropdown.add_option(option = "Settings (Ctrl+,)", command = open_settings)
    options_dropdown.add_option(option = "Close pyText (Ctrl+W)", command = close_pyText)

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

# Keyboard Shortcuts

root.bind("<Control-n>", new_file_key)
root.bind("<Control-o>", opening_file_key)
root.bind("<Control-s>", saving_key)
root.bind("<Alt-s>", saving_as_key)
root.bind("<Control-d>", discard_key)
root.bind("<Control-g>", open_source_key)
root.bind("<Control-,>", settings_key)
root.bind("<Control-w>", when_closing)

root.protocol("WM_DELETE_WINDOW", when_X_clicked)
root.config(menu = menu_bar)

root.mainloop()