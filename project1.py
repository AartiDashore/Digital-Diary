#My Digital Diary!!

from Tkinter import *
import sqlite3
import sys
sys.path.append('E:\GuDiA\Python')
from signupform import signup
from logincheck import login

def main():
    win=Tk()
    win.title("MY DIGITAL DIARY")

    lblfr=LabelFrame(win,text='Login',font='consolas')
    lblfr.grid(column=0,row=0,padx=400,pady=200)

    Label(lblfr,text='Enter the login credentials',font='consolas').grid(column=1,row=0)

    lblemailid=Label(lblfr,text='EMAILID:',font='consolas')
    lblpassword=Label(lblfr,text='PASSWORD:',font='consolas')

    entemailid=Entry(lblfr)
    entpassword=Entry(lblfr)

    lblemailid.grid(row=1)
    lblpassword.grid(row=2)
    entemailid.grid(row=1,column=1)
    entpassword.grid(row=2,column=1)

    #db=sqlite3.connect('mydigitaldiary.db')
    #db.execute('drop table if exists logintb')
    #db.execute('create table logintb(emailid text,password text,address text,phoneno int)')

    #try:
    #emaild=StringVar()
    #passwd=StringVar()

    #email=entemailid.get()
    #passwd=entpassword.get()

    loginbtn=Button(lblfr,text="LOGIN",font='consolas',command=login).grid(row=3,column=0)
    signupbtn=Button(lblfr,text="SIGN UP",font='consolas',command=signup).grid(row=3,column=1)

     #except:
         #print 'Exception occured!!!'
    
    win.mainloop()
main()
