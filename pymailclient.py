import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import *

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()

while True:
    try:
        global fromaddr
        global passw
        server.login(fromaddr, passw)
    except NameError:
        exec(open('pymaillogin.py').read())
    break

def send():
    global fromaddr
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = to.get()
    msg['Subject'] = sub.get()
    body = bodyin.get()
    msg.attach(MIMEText(body, 'plain'))
    #showinfo('Message Info', 'Message has been sent to ' + toaddr)

master = Tk()
master.title("PyMail Composer")
master.geometry('600x480')

Label(master, text="Compose").grid(column=0, row=1, sticky=W)
Label(master, text="From: " + fromaddr).grid(column=0, row=2, sticky=W)
Label(master, text="To: ",).grid(column=0, row=3, sticky=W)
Label(master, text="Subject: ",).grid(column=0, row=4, sticky=W)
Label(master, text="Body: ",).grid(column=0, row=5, sticky=W)


to = Entry(master, width=100)
to.grid(row=3, column=1)

sub = Entry(master, width=100)
sub.grid(row=4, column=1)

bodyin = Entry(master, width=100)
bodyin.grid(row=5, column=1)

Button(master, text='Send', command=send).grid(row=6, column=0, sticky=W, pady=4)

master.mainloop()

#for i in range (0,100):
#    print("\n")
#print("--------------------\nLogged In as " + fromaddr + "\n--------------------\n")

#print("Sending from " + fromaddr)
#toaddr = input("Recipient - ")



