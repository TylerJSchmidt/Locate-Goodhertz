import tkinter as tk
import os
import webbrowser

#GUI
window = tk.Tk()
window.geometry('600x500')
window.title("Goodhertz Locator")
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

#Frames
welcome = tk.Frame(window)
error = tk.Frame(window)
downloading = tk.Frame(window)
completed = tk.Frame(window)

def show_frame(frame):
    frame.tkraise()
for frame in (welcome, error, downloading, completed):
    frame.grid(row=0, column=0,sticky="nsew")
show_frame(welcome)

#Functions

#List to compare:
system_plugins = []
expected_plugins = [
    'Ghz Panpot 3.component', 'Ghz Tiltshift 3.component', 'Ghz Faraday Limiter 3.component',
    'Ghz Megaverb 3.component', 'Ghz Midside Matrix 3.component', 'Ghz Lohi 3.component',
    'Ghz Midside 3.component', 'Ghz Vulf Compressor 3.component', 'Ghz Lossy 3.component',
    'Ghz Tupe 3.component', 'Ghz Wow Control 3.component', 'Ghz Trem Control 3.component',
     'Ghz Good Dither 3.component', 'Ghz CanOpener Studio 3.component', 'Ghz Tone Control 3.component'
]

#scan_user_library() Scans the system library for installed plugins
def scan_system_library(plugin):
    for files in os.listdir(r"/Library/Audio/Plug-Ins/Components"):
        if plugin in files:
         system_plugins.append(files)
    return system_plugins

#compare_libraries() Compares the list of expected plugins vs installed plugins
def compare_librarys():
   if expected_plugins != scan_system_library("Ghz"):
       show_frame(error)
   else:
       show_frame(completed)

#download_plugins() Open's safari to "https://goodhertz.co/downloads/", clears results from system_plugins, and moves to Downloading frame
def download_plugins():
    webbrowser.open("https://goodhertz.co/downloads/")
    system_plugins.clear()
    show_frame(downloading)

#show_frame() Manages which frame is currently being shown

#Welcome
welcome_message = tk.Label(welcome, text="Hello, Welcome to Goodhertz Locator", bg="grey", width=25, height=5)
welcome_message.pack(fill='both', side=tk.TOP, expand=True)

run_btn = tk.Button(welcome, text="Run", command= lambda: compare_librarys())
run_btn.pack()

#Error
error_message = tk.Label(error, text="Plugins not found", bg="grey", width=25, height=5)
error_message.pack(fill='both', side=tk.TOP, expand=True)

download_btn = tk.Button(error, text="Download", command=lambda: download_plugins())
download_btn.pack()

#Downloading
download_message = tk.Label(downloading, text="Downloading...", bg="grey", width=25, height=5)
download_message.pack(fill='both', side=tk.TOP, expand=True)

re_run_btn = tk.Button(downloading, text="Re-run Test", command=lambda: compare_librarys())
re_run_btn.pack()

#Completed
completed_message = tk.Label(completed, text="Installation completed!", bg="grey", width=25, height=5)
completed_message.pack(fill='both', side=tk.TOP, expand=True)

frame4_btn = tk.Button(completed, text="Close", command=lambda: window.destroy())
frame4_btn.pack()

#End
window.mainloop()