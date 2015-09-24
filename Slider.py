import Tkinter
from Tkinter import *

def show_values():
    print w1.get()
number = ""

master = Tk()
w1 = Scale(master, from_=0, to=100)
w1.pack()
Button(master, text='Show', command=show_values).pack()

mainloop()