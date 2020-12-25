import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os.path
from os import path
import os
import time
from gtts import gTTS
from io import BytesIO
from playsound import playsound
from translate import Translator
master = tk.Tk() 
  
n = tk.StringVar() 
monthchoosen = ttk.Combobox(master, state="readonly", width = 7,  
                            textvariable = n) 
  
# Adding combobox drop down list 
monthchoosen['values'] = ('Bye',  
                          'Goodbye', 
                          'Goodnight', 
                          'Hello') 
  
monthchoosen.grid(column = 3, row = 4) 
monthchoosen.current()

chkValue = tk.BooleanVar() 
chkValue.set(False)
 
chkExample = tk.Checkbutton(master, text='Put Hello?', var=chkValue) 
chkExample.grid(column=3, row=3)

def show_entry_fields():
     f = open("welcome_text.txt","a")
     f.write("")
     f.close()
     lang = e2.get()
     translator = Translator(to_lang=lang)
     if monthchoosen.get() == "Bye":
      word = "Bye"
     if monthchoosen.get() == "Goodbye":
      word = "Goodbye"
     if monthchoosen.get() == "Goodnight":
      word = "Goodnight"
     if monthchoosen.get() == "Hello":
      word = "Hello"
     if not monthchoosen.get():
      word = ""
     translation = translator.translate(word)
     if chkValue.get() == False:
      f = open("welcome_text.txt","w+")
      f.write(e1.get())
      f.close()
     if chkValue.get() == True:
      f = open("welcome_text.txt","w+")
      f.write(translation + ", " + e1.get())
      f.close()
     f = open("welcome_text.txt","r")
     tts_en = gTTS(f.read(), lang=lang)
     tts_en.save('audio.mp3')
     playsound('audio.mp3')
     if os.path.isfile("audio.mp3"):
         os.remove('audio.mp3')
     else:
         show_entry_fields()


 

master.title("Welcomer")
master.geometry("300x130")

tk.Label(master, text="Name:").grid(row=0, column=3, sticky=N+S+E+W)
tk.Label(master, text="Language:").grid(row=0, column=20, sticky=N+S+E+W)

Grid.rowconfigure(master, 0, weight=1)
Grid.columnconfigure(master, 0, weight=1)

frame=Frame(master)
frame.grid(row=0, column=0, sticky=N+S+E+W)

e1 = tk.Entry(master, bg='black', fg='white')
e2 = tk.Entry(master, bg='black', fg='white')

e1.grid(row=1, column=3)
e2.grid(row=1, column=20)

canvas1 = tk.Canvas(master, width = 300, height = 130)

def ExitApplication():
    MsgBox = tk.messagebox.askquestion ('Exit Application','Are You Sure?',icon = 'warning')
    if MsgBox == 'yes':
       master.destroy()
    else:
        tk.messagebox.showinfo('Return','You will now return to the application screen')
button1 = tk.Button (master, text='Exit Application',command=ExitApplication,bg='brown',fg='white')
canvas1.create_window(150, 150, window=button1)

tk.Button(master, text='Quit', bg='black', fg='white', command=ExitApplication).grid(row=4, column=0, sticky=N+S+E+W, pady=4)
tk.Button(master, text='Create', bg='black', fg='white', command=show_entry_fields).grid(row=5, column=0, sticky=N+S+E+W, pady=4)
master.iconphoto(False, tk.PhotoImage(file='icon\icon.png'))
master.resizable(False, False)

canvas1 = tk.Canvas(master, width = 300, height = 300)

tk.mainloop()