#Signup Form

from Tkinter import *
import sqlite3

def logindatabase():
    eid1=eid
    pswd1=pswd
    add1=add
    phno1=phno

    db=sqlite3.connect('mydigitaldiary.db')
    db.execute('drop table if exists logintb')
    db.execute('create table logintb(emailid text,password text,address text,phoneno int)')
    db.execute("insert into logintb(emailid,password,address,phoneno) values ('{0}','{1}','{2}',{3})".format(eid1,pswd1,add1,phno1))
    db.commit()

    qry="select * from logintb"
    cursor=db.execute()

    for row in cursor:
        for col in row:
            print col,"\t"
        print
def signup():
    win=Tk()
    win.title("Signup form")

    eid=StringVar()
    pswd=StringVar()
    add=StringVar()
    phno=StringVar()
    
    win.geometry('1500x1400')
    sulblfr=LabelFrame(win,text='Sign Up',font='consolas')
    sulblfr.grid(row=0,column=0,padx=400,pady=200)
    
    emailid=Label(sulblfr,text='Email ID:',font='consolas').grid(row=0,column=1)
    password=Label(sulblfr,text='Password:',font='consolas').grid(row=1,column=1)
    address=Label(sulblfr,text='Address:',font='consolas').grid(row=2,column=1)
    phoneNo=Label(sulblfr,text='Phone No:',font='consolas').grid(row=3,column=1)

    entemailid=Entry(sulblfr).grid(row=0,column=2)
    entpassword=Entry(sulblfr).grid(row=1,column=2)
    entaddress=Entry(sulblfr).grid(row=2,column=2)
    entphoneNo=Entry(sulblfr).grid(row=3,column=2)

    eid=entemailid.get()
    pswd=entpassword.get()
    add=entaddress.get()
    phno=int(entphoneNo.get())

    submit=Button(sulblfr,text='SUBMIT',font='consolas',command=logindatabase).grid(row=4,column=1)
    
    win.mainloop()
