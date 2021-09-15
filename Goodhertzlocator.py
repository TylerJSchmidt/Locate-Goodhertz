import tkinter as tk
import os
import webbrowser

#Test
plugin_lib = [
    'Ghz Panpot 3.component', 'Ghz Tiltshift 3.component', 'Ghz Faraday Limiter 3.component',
    'Ghz Megaverb 3.component', 'Ghz Midside Matrix 3.component', 'Ghz Lohi 3.component',
    'Ghz Midside 3.component', 'Ghz Vulf Compressor 3.component', 'Ghz Lossy 3.component',
    'Ghz Tupe 3.component', 'Ghz Wow Control 3.component', 'Ghz Trem Control 3.component',
     'Ghz Good Dither 3.component', 'Ghz CanOpener Studio 3.component', 'Ghz Tone Control 3.component'
]
result = []
def find(name):
    for files in os.listdir(r"/Library/Audio/Plug-Ins/Components"):
        if name in files:
         result.append(files)
    return result

def click():
   if find("Ghz") != plugin_lib:
       show_frame(frame2)
       print("Plugins not found")
   else:
       show_frame(frame4)
       print("installation already completed")

#GUI
window = tk.Tk()
window.geometry('600x500')
window.title("Goodhertz Locator")
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
frame1 = tk.Frame(window)
frame2 = tk.Frame(window)
frame3 = tk.Frame(window)
frame4 = tk.Frame(window)

def show_frame(frame):
    frame.tkraise()
for frame in (frame1, frame2, frame3, frame4):
    frame.grid(row=0,column=0,sticky="nsew")
show_frame(frame1)

#=============================Welcome_Frame
frame1_title= tk.Label(frame1,text='Frame 1', bg="grey")
frame1_title.pack(fill="x")

#Greeting
greeting = tk.Label(frame1, text="Hello, Welcome to Goodhertz Locator", bg="grey", width=25, height=5)
greeting.pack(fill='both', side=tk.TOP, expand=True)
#Button
frame1_btn = tk.Button(frame1, text="Run", command= lambda: click())
frame1_btn.pack()

#=============================Error_Frame
frame2_title= tk.Label(frame2,text='Frame 2', bg="grey")
frame2_title.pack(fill="x")

#Results
greeting = tk.Label(frame2, text="Plugins not found", bg="grey", width=25, height=5)
greeting.pack(fill='both', side=tk.TOP, expand=True)

#Button2
def click2():
    webbrowser.open("https://goodhertz.co/downloads/")
    show_frame(frame3)
    result.clear()
    print(result)

frame2_btn = tk.Button(frame2, text="Download", command=lambda:click2())
frame2_btn.pack()

#=============================Download_Frame
frame3_title= tk.Label(frame3,text='Frame 3', bg="grey")
frame3_title.pack(fill="x")

#Results
greeting = tk.Label(frame3, text="Downloading...", bg="grey", width=25, height=5)
greeting.pack(fill='both', side=tk.TOP, expand=True)

frame3_btn = tk.Button(frame3, text="Re-run Test", command=lambda:click())
frame3_btn.pack()

#=============================Complete_Frame
frame4_title= tk.Label(frame4,text='Frame 4', bg="grey")
frame4_title.pack(fill="x")

#Results
greeting = tk.Label(frame4, text="Installation completed!", bg="grey", width=25, height=5)
greeting.pack(fill='both', side=tk.TOP, expand=True)

frame4_btn = tk.Button(frame4, text="Close", command=lambda:window.destroy())
frame4_btn.pack()

#End
window.mainloop()