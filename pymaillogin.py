import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import *
import pymailclient
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()

master = Tk()
master.title("PyMail - A Lightweight, Open-Source Python Based, GUI, Gmail Client")
master.geometry('600x480')


def killprogram():
    master.destroy()

def incorrect_login():
    Label(master, text="Sorry, that login was incorrect. Please try again. Take note that PyMail only works for Gmail." , height=2).grid(row=1, sticky=W)

def save_login():
    try:
        global fromaddr
        global passw
        fromaddr = e1.get()
        passw = e2.get()
        server.login(fromaddr, passw)
        killprogram()
        #exec(open('pymailclient.py').read())
        pymailclient
    except Exception:
        incorrect_login()
     
Label(master, text="Gmail Address: ").grid(row=2, sticky=W, pady=4)
Label(master, text="Password: ", height=2).grid(row=3, sticky=W)

e1 = Entry(master)
e1.grid(row=2, column=1, sticky=W)

e2 = Entry(master)
e2.grid(row=3, column=1, sticky=W)

Button(master, text='Login', command=save_login,).grid(row=4, column=0, sticky=W, pady=4)


master.mainloop()
