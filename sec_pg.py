#sec_pg.py
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import sqlite3

# Connecting to SQLite database
con = sqlite3.connect('airinfo.db')
x = con.cursor()

def nxt():
    u=user.get()
    p=passw.get()
    query='select emp_no from salespass where usern="{}" and passw="{}"'.format(u,p)
    query1='select emp_no from hrpass where usern="{}" and passw="{}"'.format(u,p)
    x.execute(query)
    f=x.fetchone()
    x.execute(query1)
    g=x.fetchone()
    if u=='':           #IF USERNAME IS NOT ENTERED
        messagebox.showerror('Error','Invalid username')
    elif p=='':         #IF PASSWORD IS NOT ENTERED
        messagebox.showerror('Error','Invalid password')
    elif f==None and g==None:
        messagebox.showerror('Error','Incorrect Username or Password')
    else:
        user_label.destroy(),user.destroy(),pass_label.destroy()
        passw.destroy(),btn.destroy()
        #COMMAND FOR HR PAGE
        def hr_pg():
            m.destroy()
            import HR      #IMPORTING HR.py 
            #COMMAND FOR SALES PAGE
        def sales_pg():
            m.destroy()
            import Sales   #IMPORTING Sales.py 
        Label(m,text='Select Department',fg='white',bg='#191970',font=('',50)).pack()
        Button(m,text="HR",command=hr_pg,font=('',40),relief='solid').pack(ipadx=130,pady=150)
        Button(m, text="Sales",command=sales_pg,font=('',40),relief='solid').pack(ipadx=100)

#CREATING NEW WINDOW
m=Tk()
m.attributes('-fullscreen',True)
m.config(bg='#191970')
user_label=Label(m,text='Username',fg='white',bg='#191970',font=('','20'))
user_label.pack(pady=30)
user=Entry(m,font=('',20))
user.pack(padx=50)
pass_label=Label(m,text='Password',fg='white',bg='#191970',font=('',20))
pass_label.pack(pady=30)
passw=Entry(m,font=('','20'),show='*')
passw.pack()
btn=Button(m,text='NEXT',font=('',40),relief='solid',command=nxt)
btn.pack(pady=30)
m.mainloop()
