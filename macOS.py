import os
try:
	from customtkinter import *
except:
	print("Installing customtkinter...")
	os.system("pip install customtkinter")
	from customtkinter import *

try:
	from CTkMessagebox import *
except:
	print("Installing CTkMessagebox...")
	os.system("pip install CTkMessagebox")
	from CTkMessagebox import *

from tkinter import filedialog, font, TkVersion
import webbrowser as web
import platform
import sys
try:
	from CTkMenuBar import *
except:
	print("Installing CTkMenuBar...")
	os.system("pip install CTkMenuBar")
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

with open("settings/keybinds/value.txt") as key_file:
    key_value = key_file.read()
    print(f"DEBUG --- Current key value is {key_value}.")

with open("settings/window/title_bar.txt") as window_file:
    title_bar = window_file.read()
    print(f"DEBUG --- Current title bar value is {title_bar}.")

if window_size == "Full Screen":
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    if platform.system() == "Windows":
        root.geometry("%dx%d+0+0" % (screenwidth, screenheight))
    else:
        root.geometry(f"{screenwidth}x{screenheight}")
else:
    root.geometry(window_size)
root.minsize(height = 100, width = 100)
root.wm_title("pyText - Untitled.txt")

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

pyText_version = "1.1.2 customtkinter build"

if theme == "dark":
    root._set_appearance_mode("dark")
elif theme == "light":
    root._set_appearance_mode("light")
else:
    root._set_appearance_mode("System")

# Functions

# Get keys from settings folder!!

def get_keys():
    # File
    global newfile_bind, openfile_bind, savefile_bind, saveas_bind, discardfile_bind
    with open("settings/keybinds/file/new_file.txt") as file:
        newfile_bind = file.read()
    with open("settings/keybinds/file/open_file.txt") as file:
        openfile_bind = file.read()
    with open("settings/keybinds/file/save_file.txt") as file:
        savefile_bind = file.read()
    with open("settings/keybinds/file/save_as.txt") as file:
        saveas_bind = file.read()
    with open("settings/keybinds/file/discard.txt") as file:
        discardfile_bind = file.read()

    # Edit
    global find_bind, replace_bind
    with open("settings/keybinds/edit/find.txt") as file:
        find_bind = file.read()
    with open("settings/keybinds/edit/replace.txt") as file:
        replace_bind = file.read()
    
    # Documentation
    global source_bind
    with open("settings/keybinds/documentation/github.txt") as file:
        source_bind = file.read()

    # Options
    global close_bind, restart_bind, settings_bind
    with open("settings/keybinds/options/close.txt") as file:
        close_bind = file.read()
    with open("settings/keybinds/options/restart.txt") as file:
        restart_bind = file.read()
    with open("settings/keybinds/options/settings.txt") as file:
        settings_bind = file.read()

def when_closing(event):
    when_X_clicked()

def when_X_clicked():
    if save_delete_used == False:
        CTkMessagebox(title = "Save first!", message = f"Save your document before closing pyText! If you would like to continue, press '{discardfile_bind}' and then close pyText.")
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
        new_window_size = f"{window_size_option.get()}"
        if title_bar == "off":
            with open("settings/window/window_size.txt", "w") as win_file:
                win_file.write(new_window_size)
                CTkMessagebox(title = "Completed", message = "Restart pyText to change the window size.")
        else:
            if new_window_size == "800x800" or new_window_size == "900x900" or new_window_size == "1000x1000" or new_window_size == "Full Screen":
                with open("settings/window/window_size.txt", "w") as win_file:
                    win_file.write(new_window_size)
                    CTkMessagebox(title = "Completed", message = "Restart pyText to change the window size.")
            else:
                question = CTkMessagebox(title = "Warning!", message = "Glitches may occor with the title bar enabled and the window size being below 800x800. Are you sure you want to proceed?", icon = "question", option_1 = "No", option_2 = "Yes")
                if question.get() == "Yes":
                    with open("settings/window/window_size.txt", "w") as win_file:
                        win_file.write(new_window_size)
                        CTkMessagebox(title = "Completed", message = "Restart pyText to change the window size.")
                else:
                    return
    
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

    def confirm_toggle_custom_keybinds():
        with open("settings/keybinds/value.txt", "w") as key_file:
            new_value = f"{customkeybinds_switch.get()}"
            key_file.write(new_value)
        if new_value == "on":
            key_frame.pack()
            confirm_btn.pack()
        else:
            key_frame.pack_forget()
            confirm_btn.pack_forget()

    def confirm_keys():
        def file_menu():
            with open("settings/keybinds/file/new_file.txt", "w") as key_file:
                keybind = newfile_entry.get()
                operator = newfile_var.get()
                key_file.write(f"{operator}-{keybind.lower()}")

            with open("settings/keybinds/file/open_file.txt", "w") as key_file:
                keybind = openfile_entry.get()
                operator = openfile_var.get()
                key_file.write(f"{operator}-{keybind.lower()}")

            with open("settings/keybinds/file/save_file.txt", "w") as key_file:
                keybind = savefile_entry.get()
                operator = savefile_var.get()
                key_file.write(f"{operator}-{keybind.lower()}")

            with open("settings/keybinds/file/open_file.txt", "w") as key_file:
                keybind = openfile_entry.get()
                operator = openfile_var.get()
                key_file.write(f"{operator}-{keybind.lower()}")
            
            with open("settings/keybinds/file/save_as.txt", "w") as key_file:
                keybind = saveasfile_entry.get()
                operator = saveasfile_var.get()
                key_file.write(f"{operator}-{keybind.lower()}")

            with open("settings/keybinds/file/discard.txt", "w") as key_file:
                keybind = discardfile_entry.get()
                operator = discardfile_var.get()
                key_file.write(f"{operator}-{keybind.lower()}")

        def edit_menu():
            with open("settings/keybinds/edit/find.txt", "w") as key_file:
                keybind = findtext_entry.get()
                operator = findtext_var.get()
                key_file.write(f"{operator}-{keybind.lower()}")

            with open("settings/keybinds/edit/replace.txt", "w") as key_file:
                keybind = replacetext_entry.get()
                operator = replacetext_var.get()
                key_file.write(f"{operator}-{keybind.lower()}")
            
        def documentation_menu():
            with open("settings/keybinds/documentation/github.txt", "w") as key_file:
                keybind = sourcecode_entry.get()
                operator = sourcecode_var.get()
                key_file.write(f"{operator}-{keybind.lower()}")

        def options_menu():
            with open("settings/keybinds/options/close.txt", "w") as key_file:
                keybind = close_entry.get()
                operator = close_var.get()
                key_file.write(f"{operator}-{keybind.lower()}")

            with open("settings/keybinds/options/restart.txt", "w") as key_file:
                keybind = restart_entry.get()
                operator = restart_var.get()
                key_file.write(f"{operator}-{keybind.lower()}")

            with open("settings/keybinds/options/settings.txt", "w") as key_file:
                keybind = settings_entry.get()
                operator = settings_var.get()
                key_file.write(f"{operator}-{keybind.lower()}")

        file_menu()
        edit_menu()
        documentation_menu()
        options_menu()

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
    tabview.add("Keybinds")
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

    # Keybinds

    CTkLabel(tabview.tab("Keybinds"), text = "Keybinds", font = (current_font, 20)).pack()

    customkeybinds_switch_value = StringVar(value = key_value)
    customkeybinds_switch = CTkSwitch(tabview.tab("Keybinds"), text = "Custom Keybinds", onvalue = "on", offvalue = "off", variable = customkeybinds_switch_value, command = confirm_toggle_custom_keybinds)
    customkeybinds_switch.pack()

    key_frame = CTkScrollableFrame(tabview.tab("Keybinds"), width = 400, height = 350)
    if theme == "dark":
        key_frame.configure(fg_color = "#252525")
    elif theme == "light":
        key_frame.configure(fg_color = "#A0A0A0")
    else:
        key_frame.configure(fg_color = "#6B6B6B")

    def one_char_limit(input_text):
        if len(input_text) > 1:
            return False
        return True
    
    get_limited = root.register(one_char_limit)

    key_options = ["Control", "Alt"]

    def find_stinky_little_disgraceful_variables_from_stinky_little_disgraceful_files(requested_keybind):
        def get_keybind(requested_keybind):
            global operator, key
            bind = menu_bar_funnies[requested_keybind]
            if bind[0] == "C":
                operator = "Control"
                key = bind[8]
            else:
                operator = "Alt"
                key = bind[4]
        if isinstance(requested_keybind, int) == True:
            get_keybind(requested_keybind)
        else:
            try:
                int(requested_keybind)
                get_keybind(requested_keybind)
            except:
                return f"Argument requested_keybind is not an interger. Please try again with an interger. requested_keybind value: {requested_keybind}"

    def make_funny_variables_to_tidy_code_by_one_billion_percent():

        # File

        global newfile_var, openfile_var, savefile_var, saveasfile_var, discardfile_var
        newfile_var = StringVar(root)
        openfile_var = StringVar(root)
        savefile_var = StringVar(root)
        saveasfile_var = StringVar(root)
        discardfile_var = StringVar(root)

        # Edit

        global findtext_var, replacetext_var
        findtext_var = StringVar(root)
        replacetext_var = StringVar(root)

        # Documentation

        global sourcecode_var
        sourcecode_var = StringVar(root)

        # Options

        global settings_var, restart_var, close_var
        settings_var = StringVar(root)
        restart_var = StringVar(root)
        close_var = StringVar(root)

    make_funny_variables_to_tidy_code_by_one_billion_percent()

    # File

    CTkLabel(key_frame, text = "File", font = (current_font, 25)).pack()

    find_stinky_little_disgraceful_variables_from_stinky_little_disgraceful_files(0)
    CTkLabel(key_frame, text = "New File", font = (current_font, 15)).pack()
    newfile_optionmenu = CTkOptionMenu(key_frame, values = key_options, variable = newfile_var)
    newfile_var.set(operator)
    newfile_optionmenu.pack()

    newfile_entry = CTkEntry(key_frame, validate = "key", validatecommand = (get_limited, "%P"))
    newfile_entry.insert(0, key)
    newfile_entry.pack()

    find_stinky_little_disgraceful_variables_from_stinky_little_disgraceful_files(1)
    CTkLabel(key_frame, text = "Open File", font = (current_font, 15)).pack()
    openfile_optionmenu = CTkOptionMenu(key_frame, values = key_options, variable = openfile_var)
    openfile_var.set(operator)
    openfile_optionmenu.pack()

    openfile_entry = CTkEntry(key_frame, validate = "key", validatecommand = (get_limited, "%P"))
    openfile_entry.insert(0, key)
    openfile_entry.pack()

    find_stinky_little_disgraceful_variables_from_stinky_little_disgraceful_files(2)
    CTkLabel(key_frame, text = "Save File", font = (current_font, 15)).pack()
    savefile_optionmenu = CTkOptionMenu(key_frame, values = key_options, variable = savefile_var)
    savefile_var.set(operator)
    savefile_optionmenu.pack()

    savefile_entry = CTkEntry(key_frame, validate = "key", validatecommand = (get_limited, "%P"))
    savefile_entry.insert(0, key)
    savefile_entry.pack()

    find_stinky_little_disgraceful_variables_from_stinky_little_disgraceful_files(3)
    CTkLabel(key_frame, text = "Save As File", font = (current_font, 15)).pack()
    saveasfile_optionmenu = CTkOptionMenu(key_frame, values = key_options, variable = saveasfile_var)
    saveasfile_var.set(operator)
    saveasfile_optionmenu.pack()

    saveasfile_entry = CTkEntry(key_frame, validate = "key", validatecommand = (get_limited, "%P"))
    saveasfile_entry.insert(0, key)
    saveasfile_entry.pack()

    find_stinky_little_disgraceful_variables_from_stinky_little_disgraceful_files(4)
    CTkLabel(key_frame, text = "Discard File", font = (current_font, 15)).pack()
    discardfile_optionmenu = CTkOptionMenu(key_frame, values = key_options, variable = discardfile_var)
    discardfile_var.set(operator)
    discardfile_optionmenu.pack()

    discardfile_entry = CTkEntry(key_frame, validate = "key", validatecommand = (get_limited, "%P"))
    discardfile_entry.insert(0, key)
    discardfile_entry.pack()

    # Edit

    CTkLabel(key_frame, text = "Edit", font = (current_font, 25)).pack()

    find_stinky_little_disgraceful_variables_from_stinky_little_disgraceful_files(5)
    CTkLabel(key_frame, text = "Find Text", font = (current_font, 15)).pack()
    findtext_optionmenu = CTkOptionMenu(key_frame, values = key_options, variable = findtext_var)
    findtext_var.set(operator)
    findtext_optionmenu.pack()

    findtext_entry = CTkEntry(key_frame, validate = "key", validatecommand = (get_limited, "%P"))
    findtext_entry.insert(0, key)
    findtext_entry.pack()

    find_stinky_little_disgraceful_variables_from_stinky_little_disgraceful_files(6)
    CTkLabel(key_frame, text = "Replace Text", font = (current_font, 15)).pack()
    replacetext_optionmenu = CTkOptionMenu(key_frame, values = key_options, variable = replacetext_var)
    replacetext_var.set(operator)
    replacetext_optionmenu.pack()

    replacetext_entry = CTkEntry(key_frame, validate = "key", validatecommand = (get_limited, "%P"))
    replacetext_entry.insert(0, key)
    replacetext_entry.pack()

    # Documentation

    CTkLabel(key_frame, text = "Documentation", font = (current_font, 25)).pack()

    find_stinky_little_disgraceful_variables_from_stinky_little_disgraceful_files(7)
    CTkLabel(key_frame, text = "Open Source Code", font = (current_font, 15)).pack()
    sourcecode_optionmenu = CTkOptionMenu(key_frame, values = key_options, variable = sourcecode_var)
    sourcecode_var.set(operator)
    sourcecode_optionmenu.pack()

    sourcecode_entry = CTkEntry(key_frame, validate = "key", validatecommand = (get_limited, "%P"))
    sourcecode_entry.insert(0, key)
    sourcecode_entry.pack()

    # Options

    CTkLabel(key_frame, text = "Options", font = (current_font, 25)).pack()

    find_stinky_little_disgraceful_variables_from_stinky_little_disgraceful_files(8)
    CTkLabel(key_frame, text = "Close pyText", font = (current_font, 15)).pack()
    close_optionmenu = CTkOptionMenu(key_frame, values = key_options, variable = close_var)
    close_var.set(operator)
    close_optionmenu.pack()

    close_entry = CTkEntry(key_frame, validate = "key", validatecommand = (get_limited, "%P"))
    close_entry.insert(0, key)
    close_entry.pack()

    find_stinky_little_disgraceful_variables_from_stinky_little_disgraceful_files(9)
    CTkLabel(key_frame, text = "Restart pyText", font = (current_font, 15)).pack()
    restart_optionmenu = CTkOptionMenu(key_frame, values = key_options, variable = restart_var)
    restart_var.set(operator)
    restart_optionmenu.pack()

    restart_entry = CTkEntry(key_frame, validate = "key", validatecommand = (get_limited, "%P"))
    restart_entry.insert(0, key)
    restart_entry.pack()

    find_stinky_little_disgraceful_variables_from_stinky_little_disgraceful_files(10)
    CTkLabel(key_frame, text = "Open pyText Settings", font = (current_font, 15)).pack()
    settings_optionmenu = CTkOptionMenu(key_frame, values = key_options, variable = settings_var)
    settings_var.set(operator)
    settings_optionmenu.pack()

    settings_entry = CTkEntry(key_frame, validate = "key", validatecommand = (get_limited, "%P"))
    settings_entry.insert(0, key)
    settings_entry.pack()

    confirm_btn = CTkButton(tabview.tab("Keybinds"), text = "Save Keybinds", command = confirm_keys)

    if key_value == "on":
        key_frame.pack()
        confirm_btn.pack()
    else:
        pass

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
        CTkMessagebox(title = "Save first!", message = f"Save your document before closing pyText! If you would like to continue, press '{discardfile_bind}' and then close pyText.")
    else:
        close_question = CTkMessagebox(title = "Would you like to close pyText?", message = "Would you like to close pyText?", icon = "question", option_1 = "No", option_2 = "Yes")
        if close_question.get() == "Yes":
            root.quit()
        else:
            return

def opening_file_key(event):
    open_file()

def open_file():
    if save_delete_used == True:
        global file_path
        file_path = filedialog.askopenfilename()
        try:
            with open(file_path, "r") as file:
                text.delete("1.0", END)
                text.insert("1.0", file.read())
                global save_path
                save_path = file_path
                root.wm_title(f"pyText - {os.path.basename(save_path)}")
        except IsADirectoryError:
            CTkMessagebox(title = "Error", message = "You have selected a directory as your file, please try again")
            open_file()
        except:
            CTkMessagebox(title = "Error", message = "An unknown error occurred, please try again.")
            return
    else:
        CTkMessagebox(title = "Warning", message = "Please save before opening a new file.", icon = "warning")

def saving_key(event):
    save_file()

def save_file():
    try:
        with open(save_path, "w") as file:
            file.write(text.get("1.0", END))
            global save_delete_used
            save_delete_used = True
            root.wm_title(f"pyText - {os.path.basename(save_path)}")
    except:
        save_as_file()

def saving_as_key(event):
    save_as_file()

def save_as_file():
    global save_path
    save_path = filedialog.asksaveasfilename(initialfile = "Untitled.txt")
    try:
        with open(save_path, "w") as file:
            file.write(text.get("1.0", END))
            global save_delete_used
            save_delete_used = True
            root.wm_title(f"pyText - {os.path.basename(save_path)}")
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
        try:
            root.destroy()
            os.system("python win-lin.py")
        except:
            try:
                root.destroy()
                os.system("py win-lin.py")
            except:
                root.destroy()
                os.system("python3 win-lin.py")

def new_file_key(event):
    new_file()

def new_file():
    if save_delete_used == False:
        CTkMessagebox(title = "Save first!", message = "Save your document before creating a new file!")
    else:
        new_file_question = CTkMessagebox(title = "New file?", message = "Would you like to create a new file, discarding the one you're currently editing?", icon="question", option_1="Cancel", option_2="No", option_3="Yes")
        if new_file_question.get() == "Yes":
            text.delete("1.0", END)
        else:
            return

def open_source():
    web.open("https://github.com/therealzakie/pyText", new = 1)

def open_source_key(event):
    open_source()

def open_readme():
    web.open("https://github.com/therealzakie/pyText/blob/master/README.md", new = 1)

def open_df_closing_safety():
    web.open("https://github.com/therealzakie/pyText/blob/master/documentation/features/closingsafety.md", new = 1)

def open_df_themes():
    web.open("https://github.com/therealzakie/pyText/blob/master/documentation/features/themes.md", new = 1)

def open_df_fonts():
    web.open("https://github.com/therealzakie/pyText/blob/master/documentation/features/font.md", new = 1)

def open_keybinds():
    web.open("https://github.com/therealzakie/pyText/blob/master/documentation/keybinds/keybinds_windows_linux.md", new = 1)

def restart_key(event):
    restart_pyText()

def restart_pyText():
    if save_delete_used == True:
        try:
            root.destroy()
            os.system("python win-lin.py")
        except:
            try:
                root.destroy()
                os.system("py win-lin.py")
            except:
                root.destroy()
                os.system("python3 win-lin.py")
    else:
        CTkMessagebox(icon = "warning", title = "Save/discard before restart!", message = "You must save/discard your file before restarting pyText!")

def find_text_key(event):
    find_text()

def find_text():
    def confirm_find():
        input = find_entry.get()
        text.tag_config("found", background = "yellow", foreground = "black")
        text.tag_remove("found", "1.0", END)
        start_ind = "1.0"
        while True:
            start_ind = text.search(input, start_ind, stopindex = END)
            if not start_ind:
                break
            last_ind = f"{start_ind}+{len(input)}c"
            text.tag_add("found", start_ind, last_ind)
            start_ind = last_ind
        
    find_window = CTkToplevel(root)
    find_window.title("Find Text")
    find_window.resizable(False, False)
    find_entry = CTkEntry(find_window, placeholder_text = "Text to find...")
    find_entry.pack()
    CTkButton(find_window, text = "Find", command = confirm_find).pack()

def replace_text_key(event):
    replace_text()

def replace_text():
    def confirm_replace():
        old_text = find_entry.get()
        new_text = replace_entry.get()
        text.tag_config("found", background = "yellow", foreground = "black")
        text.tag_remove("found", "1.0", END)
        start_ind = "1.0"
        while True:
            start_ind = text.search(old_text, start_ind, stopindex = END)
            if not start_ind:
                break
            last_ind = f'{start_ind}+{len(new_text)}c'
            text.delete(start_ind, last_ind)
            text.insert(start_ind, new_text)
            start_ind = f'{start_ind}+{len(new_text)}c'
        
    
    replace_window = CTkToplevel(root)
    replace_window.title("Replace Text")
    replace_window.resizable(False, False)
    find_entry = CTkEntry(replace_window, placeholder_text = "Text to find...")
    replace_entry = CTkEntry(replace_window, placeholder_text = "Text to replace with...")
    find_entry.pack()
    replace_entry.pack()
    CTkButton(replace_window, text = "Find & Replace", command = confirm_replace).pack()

# MenuBar

get_keys()

menu_bar_funnies = [newfile_bind, openfile_bind, savefile_bind, saveas_bind, discardfile_bind, find_bind, replace_bind, source_bind, close_bind, restart_bind, settings_bind]

if platform.system() == "Windows":
    if title_bar == "on":
        menu = CTkTitleMenu(master = root)
    else:
        if theme == "dark":
            menu = CTkMenuBar(master = root, bg_color = "#202020")
        else:
            menu = CTkMenuBar(master = root, bg_color = "#f3f3f3")

else:
    menu = CTkMenuBar(master = root)

if key_value == "off":
    file_btn = menu.add_cascade("File")
    file_dropdown = CustomDropdownMenu(widget = file_btn)
    file_dropdown.add_option(option = f"New (Control-n)", command = new_file)
    file_dropdown.add_separator()
    file_dropdown.add_option(option = f"Open (Control-o)", command = open_file)
    file_dropdown.add_separator()
    file_dropdown.add_option(option = f"Save (Control-s)", command = save_file)
    file_dropdown.add_option(option = f"Save as (Alt-s)", command = save_as_file)
    file_dropdown.add_option(option = f"Discard File (Alt-d)", command = discard_file)

    edit_btn = menu.add_cascade("Edit")
    edit_dropdown = CustomDropdownMenu(widget = edit_btn)
    edit_dropdown.add_option(option = "Copy (Control-c)", command = copy_text)
    edit_dropdown.add_option(option = "Cut (Control-x)", command = cut_text)
    edit_dropdown.add_option(option = "Paste (Control-v)", command = paste_text)
    edit_dropdown.add_separator()
    edit_dropdown.add_option(option = "Select All (Control-a)", command = select_all_text)
    edit_dropdown.add_separator()
    edit_dropdown.add_option(option = f"Find (Control-f)", command = find_text)
    edit_dropdown.add_option(option = f"Replace (Control-r)", command = replace_text)

    docs_btn = menu.add_cascade("Documentation")
    docs_dropdown = CustomDropdownMenu(widget = docs_btn)
    docs_dropdown.add_option(option = f"Source Code (Control-g)", command = open_source)
    docs_dropdown.add_option(option = "README", command = open_readme)
    docs_dropdown.add_separator()
    features_submenu = docs_dropdown.add_submenu("Features")
    features_submenu.add_option(option = "Closing Safety", command = open_df_closing_safety)
    features_submenu.add_option(option = "Editable Theme", command = open_df_themes)
    features_submenu.add_option(option = "Editable Font", command = open_df_fonts)
    docs_dropdown.add_option(option = "Keybinds", command = open_keybinds)

    options_btn = menu.add_cascade("Options")
    options_dropdown = CustomDropdownMenu(widget = options_btn)
    options_dropdown.add_option(option = f"Settings (Control-,)", command = open_settings)
    options_dropdown.add_option(option = f"Restart pyText (Alt-w)", command = restart_pyText)
    options_dropdown.add_option(option = f"Close pyText (Control-w)", command = close_pyText)

else:
    file_btn = menu.add_cascade("File")
    file_dropdown = CustomDropdownMenu(widget = file_btn)
    file_dropdown.add_option(option = f"New ({newfile_bind})", command = new_file)
    file_dropdown.add_separator()
    file_dropdown.add_option(option = f"Open ({openfile_bind})", command = open_file)
    file_dropdown.add_separator()
    file_dropdown.add_option(option = f"Save ({savefile_bind})", command = save_file)
    file_dropdown.add_option(option = f"Save as ({saveas_bind})", command = save_as_file)
    file_dropdown.add_option(option = f"Discard File ({discardfile_bind})", command = discard_file)

    edit_btn = menu.add_cascade("Edit")
    edit_dropdown = CustomDropdownMenu(widget = edit_btn)
    edit_dropdown.add_option(option = "Copy (Control-c)", command = copy_text)
    edit_dropdown.add_option(option = "Cut (Control-x)", command = cut_text)
    edit_dropdown.add_option(option = "Paste (Control-v)", command = paste_text)
    edit_dropdown.add_separator()
    edit_dropdown.add_option(option = "Select All (Control-a)", command = select_all_text)
    edit_dropdown.add_separator()
    edit_dropdown.add_option(option = f"Find ({find_bind})", command = find_text)
    edit_dropdown.add_option(option = f"Replace ({replace_bind})", command = replace_text)

    docs_btn = menu.add_cascade("Documentation")
    docs_dropdown = CustomDropdownMenu(widget = docs_btn)
    docs_dropdown.add_option(option = f"Source Code ({source_bind})", command = open_source)
    docs_dropdown.add_option(option = "README", command = open_readme)
    docs_dropdown.add_separator()
    features_submenu = docs_dropdown.add_submenu("Features")
    features_submenu.add_option(option = "Closing Safety", command = open_df_closing_safety)
    features_submenu.add_option(option = "Editable Theme", command = open_df_themes)
    features_submenu.add_option(option = "Editable Font", command = open_df_fonts)
    docs_dropdown.add_option(option = "Keybinds", command = open_keybinds)

    options_btn = menu.add_cascade("Options")
    options_dropdown = CustomDropdownMenu(widget = options_btn)
    options_dropdown.add_option(option = f"Settings ({settings_bind})", command = open_settings)
    options_dropdown.add_option(option = f"Restart pyText ({restart_bind})", command = restart_pyText)
    options_dropdown.add_option(option = f"Close pyText ({close_bind})", command = close_pyText)

# Basic text editor

text = CTkTextbox(root, undo = True, font = (current_font, current_font_size))
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

# Keyboard Shortcuts

if key_value == "off":
    root.bind("<Control-n>", new_file_key)
    root.bind("<Control-o>", opening_file_key)
    root.bind("<Control-s>", saving_key)
    root.bind("<Alt-s>", saving_as_key)
    root.bind("<Alt-d>", discard_key)
    root.bind("<Control-f>", find_text_key)
    root.bind("<Control-r>", replace_text_key)
    root.bind("<Control-g>", open_source_key)
    root.bind("<Control-,>", settings_key)
    root.bind("<Alt-w>", restart_key)
    root.bind("<Control-w>", when_closing)
else:
    root.bind(f"<{newfile_bind}>", new_file_key)
    root.bind(f"<{openfile_bind}>", opening_file_key)
    root.bind(f"<{savefile_bind}>", saving_key)
    root.bind(f"<{saveas_bind}>", saving_as_key)
    root.bind(f"<{discardfile_bind}>", discard_key)
    root.bind(f"<{find_bind}>", find_text_key)
    root.bind(f"<{restart_bind}>", replace_text_key)
    root.bind(f"<{source_bind}>", open_source_key)
    root.bind(f"<{settings_bind}>", settings_key)
    root.bind(f"<{restart_bind}>", restart_key)
    root.bind(f"<{close_bind}>", when_closing)

root.protocol("WM_DELETE_WINDOW", when_X_clicked)
root.config(menu = menu_bar)

root.mainloop()