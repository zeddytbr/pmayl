from tkinter import *
import pmaylclient

master = Tk()
master.title("PyMail - A Lightweight, Open-Source Python Based, GUI, Gmail Client")
master.geometry('600x400')

fromaddr = 0
passw = 0

def incorrect_login():
    Label(master, text="Sorry, that login was incorrect. Please try again. Take note that PyMail only works for Gmail." , height=2).grid(row=1, sticky=W)

def save_login():
    global fromaddr
    global passw
    fromaddr = str(e1.get())
    passw = str(e2.get())
    print(fromaddr + passw)
    master.destroy()
     
Label(master, text="Gmail Address: ").grid(row=2, sticky=W, pady=4)
Label(master, text="Password: ", height=2).grid(row=3, sticky=W)

e1 = Entry(master)
e1.grid(row=2, column=1, sticky=W)

e2 = Entry(master)
e2.grid(row=3, column=1, sticky=W)

Button(master, text='Login', command=save_login,).grid(row=4, column=0, sticky=W, pady=4)


master.mainloop()
