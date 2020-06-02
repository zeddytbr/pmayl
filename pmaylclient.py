#importing modules
from tkinter import *
from tkinter import messagebox

#functions
def send():
    pass

def about():
    messagebox.showinfo("Clear Names", "Are you sure you want to clear your list of inputed names?\nThis action cannot be undone!", icon="warning")
    pass

#GUI Elements
master = Tk()
master.title("PmaYl Composer")
master.geometry('600x480')

#Menu Bar
menubar = Menu(master)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

master.config(menu=menubar)

#Main Body
Label(master, text="PmaYl Composer", font="Aerial 16 bold").grid(column=0, row=10, sticky=W, pady=10)
Label(master, text="From: ").grid(column=0, row=20, sticky=W)
Label(master, text="fromaddr").grid(column=1, row=20, sticky=W)
Label(master, text="To: ",).grid(column=0, row=30, sticky=W)
Label(master, text="Subject: ",).grid(column=0, row=40, sticky=W)
Label(master, text="Body: ",).grid(column=0, row=50, sticky=W)


to = Entry(master, width=100)
to.grid(row=30, column=1)

sub = Entry(master, width=100)
sub.grid(row=40, column=1)

bodyin = Entry(master, width=100)
bodyin.grid(row=50, column=1)

Button(master, text='Send', command=send).grid(row=60, column=0, sticky=W, pady=4)

master.mainloop()