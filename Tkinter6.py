import tkinter as tk
from tkinter import ttk
import webbrowser
from tkinter import*

root = tk.Tk()
root.tittle('Universal Search Bar')

labell = ttk.Label(root, text='Query')
label.grid(row=0, column=0)
entry1 = ttk.Entry(oot, width=50)
entry1.grid(row=0, column=1)

btn2 = StringVar()

def callback():
    
    if btn2.get()=='google':
       webbrowser.open('http://google.com/search?q='+entry1.get())
    elif btn2.get() == 'duck':
         webbrowser.open('http://duckduckgo.com/search?q='+entry1.get())
         
def get(event):

    if btn2.get()=='google':
          webbrowser.open('http://google.com/search?q='+entry1.get())
    elif btn2.get() == 'duck':
         webbrowser.open('http://duckduckgo.com/search?q='+entry1.get())

MyButton1 = ttk.RadioButton(root, text='Search', width=10, command=callback)
MyButton1.grid(row=0, column=2)

entry1.bind('<Return>', get)

MyButton2 = ttk.RadioButton(root, text='Google', Value='google', variable=btn2)
MyButton2.grid(rows=1, column=1, sticky=W)

MyButton3 = ttk.Button(root, text='Duck', value='duck', variable=btn2)                      
MyButton3.grid(rows=1, column=1, stick=E)

entry1.focus()

root.wm_attributes('-topmost', 1)

root.mainloop()
