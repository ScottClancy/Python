import Tkinter
from Tkinter import *


response = ""


def ResponseIsAcceptable(pResponse):
    if(pResponse == 'Hola' or 'Hello'):
            return True
    return False

def Spanish(pSpanish):
    if(pSpanish == 'Hola'):
        return True
    return False

def French(pFrench):
    if(pFrench == 'Bonjour'):
        return True
    return False

def English(pEnglish):
    if(pEnglish == 'Hello'):
        return True
    return False


def callback():
    response = e.get()

    if ResponseIsAcceptable(response) and Spanish(response):
        print 'Hola is Spanish'
    elif ResponseIsAcceptable(response) and English(response):
        print 'Hello is English'
    elif ResponseIsAcceptable(response) and French(response):
        print 'Bonjour is French'
    else:
        print "I don't understand what you're saying"
        
master = Tk()

a = Label(master, text="Say Hi")

a.pack()


e = Entry(master)

e.pack()

e.focus_set()


b = Button(master, text="Enter", command=callback)

b.pack()

mainloop()

master = Tk()

i = Entry(master)

i.pack()

i.delete(0, END)

i.insert(0, response)


mainloop()