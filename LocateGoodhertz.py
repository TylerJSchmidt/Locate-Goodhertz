import os
import time
import threading
import subprocess
import webbrowser
from tkinter import *
from PIL import Image, ImageTk


# Checks to see if the Ghz library is installed
def ghz_library_installed():
    ghz_plugins = [
        'Ghz Panpot 3.component', 'Ghz Tiltshift 3.component', 'Ghz Faraday Limiter 3.component',
        'Ghz Megaverb 3.component', 'Ghz Midside Matrix 3.component', 'Ghz Lohi 3.component',
        'Ghz Midside 3.component', 'Ghz Vulf Compressor 3.component', 'Ghz Lossy 3.component',
        'Ghz Tupe 3.component', 'Ghz Wow Control 3.component', 'Ghz Trem Control 3.component',
        'Ghz Good Dither 3.component', 'Ghz CanOpener Studio 3.component', 'Ghz Tone Control 3.component'
    ]
    if set(ghz_plugins).issubset(os.listdir(r"/Library/Audio/Plug-Ins/Components")):
        return True


# If Ghz library installed it moves to the completed window. If not it moves to the error window.
def continue_btn_function():
    if ghz_library_installed():
        show_frame(completed_window)
    else:
        show_frame(error_window)


# Downloads Ghz library from the internet. Starts loop to test if install is complete. Moves to download window
def download_btn_function():
    show_frame(installing_window)
    threading.Thread(target=ghz_library_installed_loop).start()
    webbrowser.open("https://install.goodhertz.co/Goodhertz-Installer-3.6.2-0c0419a.pkg")


# If Ghz library installed moves to the completed window. If not displays 4 second text animation and re-runs
def ghz_library_installed_loop():
    if ghz_library_installed():
        show_frame(completed_window)
    else:
        download_title.config(text="Downloading   ")
        time.sleep(1)
        download_title.config(text="Downloading.  ")
        time.sleep(1)
        download_title.config(text="Downloading.. ")
        time.sleep(1)
        download_title.config(text="Downloading...")
        time.sleep(1)
        ghz_library_installed_loop()


# Opens a finder window to /Library/Audio/Plug-Ins/Components
def open_finder():
    subprocess.call(["open", "-R", "/Library/Audio/Plug-Ins/Components/Ghz CanOpener Studio 3.component"])


# Root Configuration
root = Tk()
root.title("")

# Center Window
app_height = 600
app_width = 900
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2 + 55)
root.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

# Windows Configuration
welcome_window = Frame(root)
error_window = Frame(root)
installing_window = Frame(root)
completed_window = Frame(root)


def show_frame(window):
    window.tkraise()


for frame in (welcome_window, error_window, installing_window, completed_window):
    frame.grid(row=0, column=0, sticky="nsew")

# Start
show_frame(welcome_window)

# Welcome Window
logo = Image.open("Logo.png")
logo = ImageTk.PhotoImage(logo)
my_logo = Label(welcome_window, image=logo)
my_logo.pack()

welcome_title = Label(welcome_window, text="Locate Goodhertz", font=("Helvetica", 30))
welcome_title.pack()

welcome_message = Label(welcome_window, text="Click continue to verify installation", font=("Helvetica", 15))
welcome_message.pack()

continue_btn = Button(welcome_window, text="Continue", font=("Helvetica", 14), command=lambda: continue_btn_function())
continue_btn.pack(pady=25)

# Error Window
error_logo = Image.open("Error.png")
error_logo = ImageTk.PhotoImage(error_logo)
my_error_logo = Label(error_window, image=error_logo)
my_error_logo.pack()

error_title = Label(error_window, text="Plugins not found", font=("Helvetica", 30))
error_title.pack()

error_message = Label(error_window, text="Click Download to install Goodhertz Plug-in Library from the web", font=("Helvetica", 15))
error_message.pack()

download_btn = Button(error_window, text="Download", font=("Helvetica", 14), command=lambda: download_btn_function())
download_btn.pack(pady=25)

# Installing Window
install_logo = Image.open("Installing.png")
install_logo = ImageTk.PhotoImage(install_logo)
my_install_logo = Label(installing_window, image=install_logo)
my_install_logo.pack()

download_title = Label(installing_window, text="", font=("Helvetica", 30))
download_title.pack()

download_message = Label(installing_window, text="Run Goodhertz Installer located in Downloads to complete installation", font=("Helvetica", 15))
download_message.pack()

# Completed Window
completed_logo = Image.open("Completed.png")
completed_logo = ImageTk.PhotoImage(completed_logo)
my_completed_logo = Label(completed_window, image=completed_logo)
my_completed_logo.pack()

completed_title = Label(completed_window, text="Verification Complete", font=("Helvetica", 30))
completed_title.pack()

completed_message = Label(completed_window, text="Library successfully installed on this system", font=("Helvetica", 15))
completed_message.pack()

finder_btn = Button(completed_window, text="Show in Finder", font=("Helvetica", 14), command=lambda: open_finder())
finder_btn.pack(side="left", padx=50)

close_btn = Button(completed_window, text="   Close   ", font=("Helvetica", 14), command=lambda: root.destroy())
close_btn.pack(side="right", padx=50)

# End
root.mainloop()